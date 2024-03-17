import requests

def get_github_user_info(username):
    # GitHub API endpoint for fetching user information
    url = f"https://api.github.com/users/{username}"
    
    # Send GET request to GitHub API
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        user_data = response.json()
        
        # Extract relevant information
        name = user_data.get('name', 'Name not available')
        bio = user_data.get('bio', 'Bio not available')
        followers = user_data.get('followers', 0)
        public_repos = user_data.get('public_repos', 0)
        
        # Print user information
        print(f"Name: {name}")
        print(f"Bio: {bio}")
        print(f"Followers: {followers}")
        print(f"Public Repositories: {public_repos}")
    else:
        print(f"Failed to fetch user information. Status code: {response.status_code}")

def main():
    # Prompt user to enter GitHub username
    username = input("Enter a GitHub username: ")
    
    # Fetch user information
    get_github_user_info(username)

if __name__ == "__main__":
    main()
