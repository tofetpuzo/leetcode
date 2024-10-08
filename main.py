from graphene import ObjectType, Field, Schema

from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField


class Query(ObjectType):
    # user = Field(User)

    def resolve_user(root, info):
        return  # get_user_by_id(12)


schema = Schema(Query)
query_string = '''
    query getUserWithFirstName {
        user {
            id
            firstName
            lastName
        }
    }
    query getUserWithFullName {
        user {
            id
            fullName
        }
    }
'''
result = schema.execute(
    query_string,
    operation_name='getUserWithFullName'
)
assert result.data['user']['fullName']


