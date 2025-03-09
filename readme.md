Here’s the completed `README.md` in proper Markdown format, structured as a typical README file with clear sections and consistent formatting. It’s ready to be dropped into your project directory.

---

```markdown
# Assignment Tracker

A sleek, dark-mode assignment tracker built with **Streamlit** to help you manage your university workload. Add assignments, track their completion, monitor progress with charts, and stay organized—all with a minimalist vibe.

---

## Features

- **Add Assignments**: Input assignment names and due dates with an intuitive form.
- **Track Progress**: Mark assignments as "Done" and see your progress with a smooth progress bar.
- **Visual Insights**: 
  - Pie chart showing the current status (Completed vs. Pending).
- **Persistent Storage**: Assignments and history are saved to a JSON file (`assignments.json`).
- **Dark Mode UI**: Custom CSS with smooth animations, hover effects, and a modern aesthetic.
- **History Tracking**: Logs actions like adding, completing, or deleting assignments.
- **Clear All**: Reset everything with a single button for a fresh start.

---

## Prerequisites

- **Python 3.8+**: Ensure Python is installed on your system.
- A terminal or command-line interface to install dependencies and run the app.

---

## Installation

1. **Clone the Repository** (or download the code):
   ```bash
   git clone <repository-url>
   cd minimalist-assignment-tracker
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   Open your browser to `http://localhost:8501` to start tracking!

---

## Usage

1. **Add an Assignment**:
   - Enter the assignment name (e.g., "CS101 Essay") and select a due date.
   - Click "Add Assignment" to save it.
2. **Track Assignments**:
   - View all assignments sorted by due date.
   - Mark them as "Done" with the checkbox or delete them with the "Delete" button.
3. **Monitor Progress**:
   - Check the progress bar and pie chart to see how you’re doing.
4. **Clear All**:
   - Hit "Clear All Assignments" to wipe the slate clean.

---

## File Structure

- `app.py`: The main application code.
- `assignments.json`: Auto-generated file to store assignments and history.
- `requirements.txt`: List of Python dependencies.
- `README.md`: This file.

---

## Dependencies

See `requirements.txt` for the full list. Key libraries include:
- `streamlit`: Web app framework.
- `matplotlib`: For generating charts.
- Standard Python libraries: `datetime`, `json`, `os`, `collections`.

---

## Screenshots

Here’s what you’ll see when you run the app:

1. **Main Interface**  
   - A dark-themed layout with a bold "Minimalist Assignment Tracker" title.
   - Below, a form to add assignments with a glowing "Add Assignment" button on hover.
   - Assignments listed in neat cards, showing due dates and days left (or "Overdue!" in red).

2. **Progress Section**  
   - A green progress bar fills up as you complete tasks.
   - A pie chart in green and red shows the split between Completed and Pending assignments.

3. **Assignment Card**  
   - Each card has a checkbox to mark "Done" and a "Delete" button that pops with a shadow effect on hover.
   - Overdue assignments stand out with red text—impossible to miss!

*Note: Add real screenshots by dragging images into your repo and linking them here (e.g., `![Main Interface](screenshots/main.png)`).*

---

## Notes

- The app saves data to `assignments.json` in the same directory. Don’t delete this file unless you want to reset everything!
- The pie chart updates dynamically based on completed and pending assignments.
- Overdue assignments are highlighted in red for quick visibility.

---

## Contributing

Feel free to fork this repo, tweak the code, or submit a pull request with improvements! Ideas:
- Add notifications for upcoming due dates.
- Include a filter for completed/pending assignments.
- Enhance the charts with more detailed stats (e.g., completion trends over time).

---

## License

This project is open-source under the [MIT License](LICENSE). Use it, modify it, share it—go wild!

---

## Built With

- Python & Streamlit
- Dark mode uni vibes 📚

Happy tracking!
```

---

### Formatting Notes
- **Headings**: Used `#` for the title and `##` for sections, following standard README conventions.
- **Code Blocks**: Wrapped commands in triple backticks (```bash) for proper syntax highlighting.
- **Lists**: Used `-` for unordered lists and `1.` for ordered steps, keeping it clean and readable.
- **Emphasis**: Applied bold (`**`) and italics (`*`) where appropriate to highlight key points or notes.
- **Separators**: Added `---` between sections for visual clarity.

This is a polished, complete README in Markdown format, ready for your project. If you need tweaks (e.g., a different tone or additional sections), just let me know!