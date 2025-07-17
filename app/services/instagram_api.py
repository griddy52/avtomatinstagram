class InstagramAPI:
    def __init__(self, access_token, proxy_url=None):
        self.access_token = access_token
        self.proxy_url = proxy_url
        # self.session = requests.Session()

    def validate_token(self):
        pass

    def create_media_container(self, video_url, caption):
        pass

    def publish_media(self, creation_id):
        pass

    def get_container_status(self, container_id):
        pass 