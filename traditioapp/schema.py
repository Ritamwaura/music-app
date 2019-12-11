import graphene
from graphene_django import DjangoObjectType

from .models import Profile, Traditonsongs, Songs, LatestContact, Post


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class traditiontradType(DjangoObjectType):
    class Meta:
        model = Traditonsongs


class SongsType(DjangoObjectType):
    class Meta:
        model = Songs


class LatestType(DjangoObjectType):
    class Meta:
        model = LatestContact


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class Query(graphene.ObjectType):
    profiles = graphene.List(ProfileType)
    traditiontrads = graphene.List(traditiontradType)
    songses = graphene.List(SongsType)
    late = graphene.List(LatestType)
    posts = graphene.List(PostType)

    def resolve_profiles(self, info, **kwargs):
        return Profile.objects.all()

    def resolve_traditiontrads(self, info, **kwargs):
        return Traditonsongs.objects.all()

    def resolve_songses(self, info, **kwargs):
        return Songs.objects.all()

    def resolve_late(self, info, **kwargs):
        return LatestContact.objects.all()

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()


schema = graphene.Schema(query=Query, subscription=Query)
