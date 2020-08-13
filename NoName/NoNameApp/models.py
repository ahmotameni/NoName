import datetime

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True, primary_key=True)
    password = models.CharField(max_length=10)

    first_name = models.CharField(max_length=20, default=None)
    last_name = models.CharField(max_length=20, default=None)

    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('P', 'Prefer not to say'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    phone_number = models.CharField(max_length=12, default=None, unique=True)
    email = models.EmailField(default=None, unique=True)

    birthday = models.DateTimeField(default=None)

    join_date = models.DateTimeField()

    def __str__(self):
        return self.username


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")

    class Meta:
        unique_together = ('follower', 'followed')

    date = models.DateTimeField()

    def __str__(self):
        return self.follower.username + " follows " + self.followed.username


class Poll(models.Model):
    poll_phrase = models.CharField(max_length=100, primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    date_created = models.DateTimeField()

    def __str__(self):
        return self.poll_phrase


class Choice(models.Model):
    choice_text = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.choice_text


class PollChoice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('poll', 'choice')

    num_votes = models.IntegerField()
    sum_votes = models.IntegerField()
    avg_point = models.FloatField()

    def __str__(self):
        return self.poll.__str__() + "," + self.choice.__str__()


class Vote(models.Model):
    poll_choice = models.ForeignKey(PollChoice, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.voter.__str__() + " voted on " + self.poll_choice.__str__()

    class Meta:
        unique_together = ('poll_choice', 'voter')

    POINT_CHOICES = (
        (-5, -5),
        (-4, -4),
        (-3, -3),
        (-2, -2),
        (-1, -1),
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    point = models.IntegerField(choices=POINT_CHOICES)

    date = models.DateTimeField()

    comment = models.CharField(max_length=1000)
