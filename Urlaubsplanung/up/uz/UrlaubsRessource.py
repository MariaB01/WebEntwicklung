import json
import falcon
from up.uz.UrlaubsService import UrlaubsService



class UrlaubRessource:
    def on_get_urlaubsziele(self, req, resp):
        urlaub_list = UrlaubsService.get_urlaubsziele()
        resp.text = json.dumps([v.to_dict() for v in urlaub_list], ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200



    def on_get_urlaubsziel(self, req, resp, uzid):
        resp.text = None
        uz = UrlaubsService.get_urlaubsziel(int(uzid))
        resp.text = json.dumps(uz.to_dict(), ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

   # def on_get_videosbygenre(self, req, resp, genre):
    #    video_list = VideoService.get_videos_by_genre(genre)
     #   resp.text = json.dumps([v.to_dict() for v in video_list], ensure_ascii=False, indent=2)

    #def on_get_videosbyagerating(self, req, resp, age_rating):
     #   video_list = VideoService.get_videos_by_age_rating(age_rating)
      #  resp.text = json.dumps([v.to_dict() for v in video_list], ensure_ascii=False, indent=2)

   # def on_get_videogenres(self, req, resp):
    #    genre_list = VideoService.get_video_genres()
     #   result = [{"genre": row[0]} for row in genre_list]
      #  resp.text = json.dumps(result, ensure_ascii=False, indent=2)

    #def on_get_videonumbers(self, req, resp):
     #   vnr_list = VideoService.get_video_numbers()
      #  result = [row[0] for row in vnr_list]
       # resp.text = json.dumps(result, ensure_ascii=False, indent=2)

    def on_post_urlaubsziel(self, req, resp):
        uz_json = json.load(req.bounded_stream)
        UrlaubsService.create_urlaubsziel(uz_json)
        resp.text = "Urlaubsziel added successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_put_urlaubsziel(self, req, resp, uzid):
        uz_json = json.load(req.bounded_stream)
        UrlaubsService.update_urlaubsziel(int(uzid), uz_json)
        resp.text = f"Urlaubsziel with the ID {uzid} updated successfully!"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT


    def on_delete_urlaubsziel(self, req, resp, uzid):
        UrlaubsService.delete_urlaubsziel(int(uzid))
        resp.text = f"Urlaubsziel with the ID {uzid} deleted successfully!"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT
