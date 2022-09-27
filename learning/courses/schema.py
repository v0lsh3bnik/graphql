import graphene
from graphene_django.types import DjangoObjectType
from .models import ParametreContrat


class ContractType(DjangoObjectType):
    class Meta:
        model = ParametreContrat


class GetContrat(graphene.ObjectType):
    contracts = graphene.List(ContractType)

    def resolve_contracts(self, info, **kwargs):
        print("***********************************************")
        return ParametreContrat.objects.all()


class Query(
    GetContrat,
    graphene.ObjectType
):
    pass


class Mutation(
    GetContrat,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
