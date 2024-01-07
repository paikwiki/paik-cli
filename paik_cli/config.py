class AppConfig:
    def __init__(
        self, memo_folder_path, jira_url, exclude_h1_titles=[], titles_for_summary=[]
    ):
        self.memo_folder_path = memo_folder_path
        self.jira_url = jira_url
        self.exclude_h1_titles = exclude_h1_titles
        self.titles_for_summary = titles_for_summary
