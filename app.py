import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('YouTube Trending Video Analysis')

df = pd.read_csv('processed_data.csv')

st.subheader('Raw Data')
st.write(df.head())

st.subheader('Views Distribution')
fig, ax = plt.subplots()
sns.histplot(df['views'], bins=50, color='purple', ax=ax)
st.pyplot(fig)

st.subheader('Average Views by Category')
avg_views = df.groupby('category_id')['views'].mean().sort_values(ascending=False)
st.bar_chart(avg_views)

st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(df[['views', 'likes', 'comment_count', 'dislikes']].corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.subheader("Top 10 Channels by Views")
top_channels = df.groupby('channel_title')['views'].sum().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=top_channels.values, y=top_channels.index, palette='viridis', ax=ax)
st.pyplot(fig)

st.subheader("Average Views by Publish Hour")
publish_hour = df.groupby('publish_hour')['views'].mean()
fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(x=publish_hour.index, y=publish_hour.values, marker='o', ax=ax)
ax.set_xticks(range(0,24))
st.pyplot(fig)

st.subheader("Comments vs Likes")
fig, ax = plt.subplots(figsize=(8,6))
sns.scatterplot(data=df, x='comment_count', y='likes', alpha=0.5, ax=ax)
ax.set_xscale('log')
ax.set_yscale('log')
st.pyplot(fig)
