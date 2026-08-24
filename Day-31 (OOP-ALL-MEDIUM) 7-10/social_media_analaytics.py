'''
Medium Problem 10 – Social Media Analytics Dashboard
Context A social media manager tracks posts across platforms. Each post has engagement metrics (likes, shares, comments). The system calculates reach, engagement rate, and best‑performing post types.

Task Create the following classes:

Post

Attributes: content, platform (FB, IG, X), timestamp.
Private: __likes, __shares, __comments.
Methods: add_like(), add_share(), add_comment().
engagement_score() – likes + shares*2 + comments*3.
VideoPost (inherits Post)

Adds duration, views.
Override engagement_score() – add views * 0.1.
ImagePost (inherits Post)

Adds hashtags (list).
Override engagement_score() – add len(hashtags) * 5.
AnalyticsDashboard

Manages __posts (list).
Methods: add_post(post).
average_engagement_by_platform() – returns dict.
top_posts(n) – returns top n posts by engagement.
trending_hashtags() – for ImagePosts, returns most common hashtags.
ReportGenerator (static)

Static method: generate_report(dashboard, start_date, end_date) – returns summary dict.
Additional

Use class variable POST_ID to auto‑assign IDs.
Override __lt__ to compare posts by engagement.
Use @staticmethod for date parsing.
Sample Usage

db = Dashboard()
p1 = ImagePost("Sunset!", "IG", "2026-08-01", hashtags=["#nature", "#sunset"])
p1.add_like(); p1.add_like(); p1.add_share()
db.add_post(p1)
print(db.average_engagement_by_platform())  # {"IG": score}
top = db.top_posts(1)
print(top[0].content)
'''


class Post:
  def __init__(self,content,platform,timestamp):
    self.content = content
    self.platform = platform
    self.timestamp = timestamp
    self.__likes = 0

    self.__shares = 0
    self.__comments = 0


  def add_like(self):
    self.__likes+=1

  def add_share(self):
    self.__shares+=1

  def add_comment(self):
    self.__comments+=1

  def engagement_score(self):
    return (self.__likes) + (self.__shares*2) + (self.__comments*3)

  def __lt__(self,others):
    return self.engagement_score() < others.engagement_score()


class VideoPost(Post):
  def __init__(self,content,platform,timestamp,duration,views):
    super().__init__(content,platform,timestamp)
    self.duration = duration
    self.views = views

  def engagement_score(self):
    return super().engagement_score() + self.views * 0.1

class ImagePost(Post):
  def __init__(self,content,platform,timestamp,hashtags):
    super().__init__(content,platform,timestamp)
    self.hashtags = hashtags

  def engagement_score(self):
    return super().engagement_score() + len(self.hashtags) * 5


class Dashboard():
  def __init__(self):
    self.__posts = []

  def get_posts(self):
    p = []
    for i in self.__posts:
      p.append(i)
    return p

  def add_post(self,post):
    if post not in self.__posts:
      self.__posts.append(post)
      return True
    return False

  def top_posts(self,n):
    count = 0
    result = []
    sorted_posts = sorted(self.__posts, key=lambda obj: obj.engagement_score(),reverse=True)

    for i in sorted_posts:
      if n > count:
        result.append(i)
        count+=1
    return result

  def trending_hashtags(self):
    d = {}
    for i in self.__posts:
      if isinstance(i,ImagePost):
        for tag in i.hashtags:
          if tag not in d:
            d[tag]=1
          else:
            d[tag]+=1
    sorted_d = sorted(d.items(), key=lambda item: item[1],reverse=True)
    return sorted_d

  def average_engagement_by_platform(self):
    d = {}
    for post in self.__posts:
      if post.platform not in d:
        d[post.platform] = post.engagement_score()
      else:
        d[post.platform] = (post.engagement_score() + d[post.platform])/2
    return d


db = Dashboard()
p1 = ImagePost("Sunset!", "IG", "2026-08-01", hashtags=["#nature", "#sunset"])
p1.add_like(); p1.add_like(); p1.add_share()
db.add_post(p1)
print(db.average_engagement_by_platform())  # {"IG": score}
top = db.top_posts(1)
print(top[0].content)
