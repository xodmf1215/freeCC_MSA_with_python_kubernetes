import pika, json, tempfile, os
from bson.objectid import ObjectId
import moviepy.editor

def start(message, fs_videos, fs_mp3s, channel):
    ''' convert to mp3 start, message: mongodb, fs_video: gridfs(db), fs_mp3: gridfs(db) '''
    message = json.loads(message)

    # empty temp file
    tf = tempfile.NamedTemporaryFile()
    # get video contents from mongodb with video_fid that was given when uploads the video
    out = fs_videos.get(ObjectId(message["video_fid"]))
    # add video contentsto empty file
    tf.write(out.read())
    # create audio from temp video file
    audio = moviepy.editor.VideoFileClip(tf.name).audio
    tf.close()

    # write audio to the file
    tf_path = tempfile.gettempdir() + f"/{message['video_fid']}.mp3"

    audio.write_audiofile(tf_path)

    # save file to mongo
    f = open(tf_path, "rb")
    data = f.read()
    fid = fs_mp3s.put(data)
    f.close()
    # delete temp file
    os.remove(tf_path)

    message["mp3_fid"] = str(fid)

    try:
        channel.basic_publish(
            exchange="",
            routing_key= os.environ.get("MP3_QUEUE"),
            body = json.dumps(message),
            properties= pika.BasicProperties(
                delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as error:
        fs_mp3s.delete(fid)
        return "failed to publish message"