import graphene
from graphene_django import DjangoObjectType
from .models import Image
from graphene_file_upload.scalars import Upload


class ImageType(DjangoObjectType):
    class Meta:
        model = Image
        fields = ('id','title', 'image','created_at')

class Query(graphene.ObjectType):
  """
  Queries for the Image model
  """
  images = graphene.List(ImageType)

  def resolve_images(self, info, **kwargs):
    return Image.objects.all()

class CreateImage(graphene.Mutation):
  class Arguments:
    title = graphene.String(required="True")
    image = Upload(required="True")

  ok = graphene.Boolean()
  image = graphene.Field(ImageType)

  def mutate(self, info, title, image):

      image = Image(title=title, image=image)
      image.save()
      return CreateImage(ok=True, image=image)


class DeleteImage(graphene.Mutation):
  class Arguments:
    id = graphene.Int()

  ok = graphene.Boolean()

  def mutate(self, info, id):
    restaurant = Image.objects.get(id=id)
    restaurant.delete()
    return DeleteImage(ok=True)

class UpdateImage(graphene.Mutation):
  class Arguments:
    id = graphene.Int()
    title = graphene.String()
    image = graphene.String()

  ok = graphene.Boolean()
  image = graphene.Field(ImageType)

  def mutate(self, info, id, title, image):
    image = Image.objects.get(id=id)
    image.title = title
    if image:
        image = image
    image.save()
    return UpdateImage(ok=True, image=image)

class Mutation(graphene.ObjectType):
  create_image = CreateImage.Field()
  delete_image = DeleteImage.Field()
  update_image = UpdateImage.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
