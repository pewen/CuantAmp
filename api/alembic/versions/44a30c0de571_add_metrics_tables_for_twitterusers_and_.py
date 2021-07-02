"""Add metrics tables for TwitterUsers and Tweets

Revision ID: 44a30c0de571
Revises: 1c3642bfed05
Create Date: 2021-07-01 16:32:22.982616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44a30c0de571'
down_revision = '1c3642bfed05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweets_metrics',
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('time', sa.DateTime(), nullable=False),
        sa.Column('tweet_id', sa.Integer(), nullable=False),
        sa.Column('quote_count', sa.Integer(), nullable=True),
        sa.Column('reply_count', sa.Integer(), nullable=True),
        sa.Column('retweet_count', sa.Integer(), nullable=False),
        sa.Column('favorite_count', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['tweet_id'], ['tweets.id'], ),
        sa.PrimaryKeyConstraint('id', 'time')
    )
    op.create_index(
        op.f('ix_tweets_metrics_id'),
        'tweets_metrics',
        ['id'],
        unique=False
    )
    op.create_index(
        op.f('ix_tweets_metrics_time'),
        'tweets_metrics',
        ['time'],
        unique=False
    )
    op.create_index(
        op.f('ix_tweets_metrics_tweet_id'),
        'tweets_metrics',
        ['tweet_id'],
        unique=False
    )
    # op.execute("SELECT create_hypertable('tweets_metrics','time');")

    op.create_table('twitter_users_metrics',
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('time', sa.DateTime(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('followers_count', sa.Integer(), nullable=False),
        sa.Column('friends_count', sa.Integer(), nullable=False),
        sa.Column('listed_count', sa.Integer(), nullable=False),
        sa.Column('favourites_count', sa.Integer(), nullable=False),
        sa.Column('statuses_count', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['twitter_users.id'], ),
        sa.PrimaryKeyConstraint('id', 'time'),
    )
    op.create_index(
        op.f('ix_twitter_users_metrics_id'),
        'twitter_users_metrics',
        ['id'],
        unique=False
    )
    op.create_index(
        op.f('ix_twitter_users_metrics_time'),
        'twitter_users_metrics',
        ['time'],
        unique=False
    )
    op.create_index(
        op.f('ix_twitter_users_metrics_user_id'),
        'twitter_users_metrics',
        ['user_id'],
        unique=False
    )
    op.execute("SELECT create_hypertable('twitter_users_metrics','time');")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f('ix_twitter_users_metrics_user_id'),
        table_name='twitter_users_metrics'
    )
    op.drop_index(
        op.f('ix_twitter_users_metrics_time'),
        table_name='twitter_users_metrics'
    )
    op.drop_index(
        op.f('ix_twitter_users_metrics_id'),
        table_name='twitter_users_metrics'
    )
    op.drop_table('twitter_users_metrics')

    op.drop_index(
        op.f('ix_tweets_metrics_tweet_id'),
        table_name='tweets_metrics'
    )
    op.drop_index(
        op.f('ix_tweets_metrics_time'),
        table_name='tweets_metrics'
    )
    op.drop_index(
        op.f('ix_tweets_metrics_id'),
        table_name='tweets_metrics'
    )
    op.drop_table('tweets_metrics')
    # ### end Alembic commands ###
