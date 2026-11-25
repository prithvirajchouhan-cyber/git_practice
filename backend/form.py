class RequestForm:
    def __init__(self, data):
        self.data = data
        self.errors = {}

    def is_valid(self):
        self.errors = {}

        title = self.data.get("title", "").strip()
        description = self.data.get("description", "").strip()

        if not title:
            self.errors["title"] = "Title is required"

        if not description:
            self.errors["description"] = "Description is required"

        if len(title) > 100:
            self.errors["title"] = "Title cannot exceed 100 characters"

        return len(self.errors) == 0