import graphene
from graphene_django import DjangoObjectType
from crm.models import Customer 


# 1. Define a GraphQL Type for Customer
class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "email", "phone")


# 2. Extend Query with customers list
class Query(graphene.ObjectType):
    hello = graphene.String()
    customers = graphene.List(CustomerType)

    def resolve_hello(root, info):
        return "Hello, GraphQL!"

    def resolve_customers(root, info):
        return Customer.objects.all()


# 3. Final schema
schema = graphene.Schema(query=Query)

