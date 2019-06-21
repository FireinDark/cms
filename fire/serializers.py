# -*- coding: utf-8 -*-
import models
from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Article
        fields = ['title', 'author', 'content','column','author','user', ' pub_date']
