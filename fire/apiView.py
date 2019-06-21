# -*- coding: utf-8 -*-
# 专门用来放api接口的地方

import models
from fire.serializers import ArticleSerializer
from rest_framework import viewsets


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.order_by('id').all()
    serializer_class = ArticleSerializer
