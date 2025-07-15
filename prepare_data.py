import os

def combine_user_data(username):
    post_path = f"output/{username}_posts.txt"
    comment_path = f"output/{username}_comments.txt"
    combined_path = f"output/{username}_combined.txt"

    if not os.path.exists(post_path) or not os.path.exists(comment_path):
        print("❌ Post or comment file not found.")
        return

    with open(post_path, "r", encoding="utf-8") as p, \
         open(comment_path, "r", encoding="utf-8") as c, \
         open(combined_path, "w", encoding="utf-8") as out:

        out.write("=== REDDIT POSTS ===\n\n")
        out.write(p.read())
        out.write("\n\n=== REDDIT COMMENTS ===\n\n")
        out.write(c.read())

    print(f"✅ Combined data saved to: {combined_path}")


if __name__ == "__main__":
    combine_user_data("kojied")
