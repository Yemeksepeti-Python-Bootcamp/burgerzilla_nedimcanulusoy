"""init

Revision ID: 57b09b39797a
Revises: 
Create Date: 2022-02-13 22:42:33.583781

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '57b09b39797a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=50), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name'),
                    schema='bzschema'
                    )
    op.create_table('roles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=50), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name'),
                    schema='bzschema'
                    )
    op.create_table('token_block_list',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('jti', sa.String(length=36), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    schema='bzschema'
                    )
    op.create_table('menu',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=50), nullable=False),
                    sa.Column('price', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(length=100), nullable=False),
                    sa.Column('image', sa.String(length=120), nullable=False),
                    sa.Column('restaurant_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['restaurant_id'], ['bzschema.restaurant.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='bzschema'
                    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=50), nullable=False),
                    sa.Column('surname', sa.String(length=50), nullable=False),
                    sa.Column('username', sa.String(length=50), nullable=False),
                    sa.Column('email', sa.String(length=50), nullable=False),
                    sa.Column('password_hash', sa.String(length=128), nullable=False),
                    sa.Column('address', sa.String(length=120), nullable=False),
                    sa.Column('restaurant_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['restaurant_id'], ['bzschema.restaurant.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('username'),
                    schema='bzschema'
                    )
    op.create_table('order',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('status', sa.String(length=50), nullable=False),
                    sa.Column('timestamp', sa.String(length=25), nullable=True),
                    sa.Column('restaurant_id', sa.Integer(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['restaurant_id'], ['bzschema.restaurant.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['bzschema.user.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='bzschema'
                    )
    op.create_table('user_roles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('role_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['role_id'], ['bzschema.roles.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['bzschema.user.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    schema='bzschema'
                    )
    op.create_table('order_menu',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('order_id', sa.Integer(), nullable=True),
                    sa.Column('menu_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['menu_id'], ['bzschema.menu.id'], ),
                    sa.ForeignKeyConstraint(['order_id'], ['bzschema.order.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='bzschema'
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_menu', schema='bzschema')
    op.drop_table('user_roles', schema='bzschema')
    op.drop_table('order', schema='bzschema')
    op.drop_table('user', schema='bzschema')
    op.drop_table('menu', schema='bzschema')
    op.drop_table('token_block_list', schema='bzschema')
    op.drop_table('roles', schema='bzschema')
    op.drop_table('restaurant', schema='bzschema')
    # ### end Alembic commands ###
