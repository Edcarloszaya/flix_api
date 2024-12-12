from django.db.models import Avg
from rest_framework import serializers

from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError(
                "A data de lacamento nao poder ser menor quer 1990"
            )
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError(
                "Resumo nao pode ser maior que 200 caracteres."
            )
        return value


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()


class MovieListDetailserializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()

    class Meta:
        model = Movie
        fields = ["id", "title", "genre", "actors", "release_date", "rate", "resume"]

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]
        if rate:
            return rate
        return None
