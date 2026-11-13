from dataclasses import dataclass
from drafter import *


# Site details required by the project (shown on the site's About page).
set_website_title("Campus Connect")
set_site_information(
    author="Stephen Daoud",
    description=("Campus Connect helps students see when friends are free "
                 "and plan activities."),
    sources=["Drafter documentation: https://drafter-edu.github.io/drafter/",
             "AI help from ChatGPT (conversations are in this repository)"],
    planning="Pages: Home, Calendar, Friends, Suggest Activity, and Inbox.",
    links=[]
)
# Release settings from Drafter's GitHub Pages guide.
hide_debug_information()
set_website_framed(False)

# add_website_css adds CSS styling rules (colors, spacing, the scrolling
# calendar grid). CSS was not covered in class; it only changes the look.
add_website_css("""
body { background: #f3f6fb; color: #172b45; font-family: Arial, sans-serif; }
h1, h2, h3 { color: #123d70; }
button { border-radius: 8px; cursor: pointer; padding: 9px 13px; }
.site-nav { background: #123d70; padding: 15px; border-radius: 12px;
            display: flex; flex-wrap: wrap; align-items: center; gap: 18px;
            margin-bottom: 24px; }
.site-nav a { color: white; font-weight: bold; text-decoration: none; }
.site-nav a:hover { color: #ffd166; }
.brand { color: #ffd166; font-size: 22px; font-weight: bold; margin-right: 12px; }
.panel, .hero, .invite-card { background: white; border: 1px solid #dce4ed;
            padding: 19px; border-radius: 12px; margin: 12px 0;
            box-shadow: 0 3px 12px #123d7010; }
.hero { border-left: 6px solid #efbd46; }
.stats { display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0; }
.stat { flex: 1; min-width: 145px; padding: 18px;
        background: white; border-radius: 12px; border-top: 4px solid #efbd46; }
.stat h3 { margin: 0; font-size: 26px; }
.table-wrap { width: 100%; max-width: 100%; box-sizing: border-box;
              overflow-x: auto; }
.calendar-scroll { height: 65vh; max-height: 600px; overflow: auto !important;
                   padding: 0 !important; scrollbar-width: auto;
                   scrollbar-color: #bf8b25 #e9f0fa; }
/* A CSS grid keeps both sticky directions inside the SAME scrolling box. */
.calendar-grid { display: grid !important;
                 grid-template-columns: 90px repeat(7, 133px);
                 grid-auto-rows: minmax(48px, auto); width: max-content; }
.calendar-grid > div, .calendar-grid > button {
    box-sizing: border-box; border: 1px solid #d4e0ed;
    display: flex; align-items: center; justify-content: center;
    padding: 8px; text-align: center; }
.calendar-grid .calendar-day { position: sticky !important; top: 0; z-index: 3;
    background: #e8f0fa !important; color: #113b66 !important;
    font-weight: bold; }
.calendar-grid .calendar-time { position: sticky !important; left: 0; z-index: 2;
    background: #dbe8f7 !important; color: #102f52 !important;
    font-weight: bold; white-space: nowrap; }
.calendar-grid .calendar-corner { position: sticky !important;
    top: 0; left: 0; z-index: 4;
    background: #dbe8f7 !important; color: #102f52 !important;
    font-weight: bold; }
.calendar-grid button.free-slot, .calendar-grid button.free-slot:hover {
    border-radius: 0; background: #d5f1e0 !important;
    color: #125737 !important; font-weight: bold; }
.calendar-grid button.empty-slot, .calendar-grid button.empty-slot:hover {
    border-radius: 0; background: #f2f6fc !important;
    color: #163c65 !important; font-weight: bold; }
.calendar-scroll::-webkit-scrollbar { width: 12px; height: 12px; }
.calendar-scroll::-webkit-scrollbar-track { background: #e9f0fa; }
.calendar-scroll::-webkit-scrollbar-thumb {
    background: #bf8b25; border-radius: 10px; border: 2px solid #e9f0fa; }
.scroll-hint { color: #123d70; font-weight: bold; padding: 8px 0; }
/* Explicit colors keep the calendar readable with any Drafter theme. */
.table-wrap table { width: 100%; border-collapse: collapse;
                    background: #ffffff !important; color: #173451 !important; }
.table-wrap table th { background: #e8f0fa !important; color: #113b66 !important;
                       font-weight: bold; }
.table-wrap table td { background: #ffffff !important; color: #173451 !important; }
.table-wrap table th, .table-wrap table td {
    padding: 9px; border: 1px solid #d4e0ed; text-align: center; }
/* Keep time labels visible when the calendar scrolls sideways. */
.table-wrap table th:first-child, .table-wrap table td:first-child {
    background: #dbe8f7 !important; color: #102f52 !important;
    font-weight: bold; min-width: 82px; white-space: nowrap;
    position: sticky; left: 0; z-index: 1; }
.table-wrap table button.free-slot, .table-wrap table button.empty-slot {
    width: 100%; min-width: 66px; font-size: 13px; font-weight: bold;
    opacity: 1 !important; text-shadow: none !important; }
.table-wrap table button.free-slot, .table-wrap table button.free-slot:hover {
    background: #d5f1e0 !important; color: #125737 !important;
    border: 1px solid #89c9a6 !important; }
.table-wrap table button.empty-slot, .table-wrap table button.empty-slot:hover {
    background: #f2f6fc !important; color: #163c65 !important;
    border: 1px solid #bdcfe4 !important; }
.both-free { background: #d9f3e1; color: #17643a; padding: 6px; border-radius: 6px; }
.you-free { background: #deebfa; color: #174c83; padding: 6px; border-radius: 6px; }
.friend-free { background: #fff0ca; color: #765011; padding: 6px; border-radius: 6px; }
.status { display: inline-block; font-weight: bold; padding: 5px 10px;
          border-radius: 20px; background: #fff0ca; color: #775013; }
.accepted { background: #d9f3e1; color: #17643a; }
.declined { background: #fbe2e2; color: #973333; }
.muted { color: #64748b; }
""")


# Sample students and available time choices.
STUDENTS = ["Alex", "Sam", "Jordan"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
TIMES = ["8 AM", "9 AM", "10 AM", "11 AM", "12 PM",
         "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM",
         "7 PM", "8 PM", "9 PM", "10 PM"]
ACTIVITIES = ["Coffee", "Study", "Gym", "Food"]


@dataclass
class ActivityInvitation:
    """Keep the details of one invitation in one place.

    Fields:
        sender: The student who sends the invitation, such as Alex.
        receiver: The student invited to the activity, such as Sam.
        activity: What they want to do, such as Coffee or Study.
        day: The day they want to meet, such as Tuesday.
        time: The time they want to meet, such as 4 PM.
        status: Whether the invite is Pending, Accepted, or Declined.
            New invitations start as Pending.

    Each invitation is one object inside State.invitations. Its status
    can change when the invited student accepts or declines.
    """
    sender: str
    receiver: str
    activity: str
    day: str
    time: str
    status: str = "Pending"


@dataclass
class State:
    """Store the information the website needs between button clicks.

    Fields:
        session: The name of the currently signed-in student.
        selected_day: The last day used when adding or removing free time.
        available_slots: A dictionary with one list of free times for each
            student. For example, Alex might have ["Tuesday at 4 PM"].
        invitations: A list of ActivityInvitation objects, including their
            senders, receivers, times, and current statuses.

    The website passes this same State object between its pages. Routes
    can change its fields to remember schedules and invitations.
    """
    session: str
    selected_day: str
    available_slots: dict[str, list[str]]
    invitations: list[ActivityInvitation]


def menu() -> list:
    """Make the blue navigation bar with links to the five pages.

    Parameters: None.
    Returns: A list containing the navigation bar for a Drafter page.
    Changes: Nothing in State. This only builds page content.
    """
    return [
        Div(
            Span("CC", classes="brand"),
            Link("Home", "navigate", [Argument("destination", "index")]),
            Link("Calendar", "navigate", [Argument("destination", "calendar")]),
            Link("Friends", "navigate", [Argument("destination", "friends")]),
            Link("Suggest Activity", "navigate", [Argument("destination", "suggest")]),
            Link("Inbox", "navigate", [Argument("destination", "inbox")]),
            classes="site-nav"
        ),
    ]


@route
def navigate(state: State, destination: str, student: str = "", friend: str = "",
             activity: str = "", day: str = "", time: str = "") -> Page:
    """Open the page chosen in the navigation bar.

    Parameters:
        state: The information the website is remembering.
        destination: The page to open, such as calendar or inbox.
        student, friend, activity, day, time: Extra choices that might be
            submitted from the page being left. They are ignored here.
    Returns: The requested Drafter Page, or Home for an unknown name.
    Changes: Nothing in State. It only chooses which page to show.
    """
    if destination == "calendar":
        return calendar(state)
    if destination == "friends":
        return friends(state)
    if destination == "suggest":
        return suggest(state)
    if destination == "inbox":
        return inbox(state)
    return index(state)


@route
def index(state: State) -> Page:
    """Show the Home dashboard for the student who is signed in.

    Parameters:
        state: The signed-in student, schedules, and invitations.
    Returns: The Home Page with a sign-in choice and three totals.
    Changes: Nothing in State. The totals are counted from existing data.
    """
    pending = 0
    accepted = 0
    for invitation in state.invitations:
        if invitation.receiver == state.session and invitation.status == "Pending":
            pending = pending + 1
        if (invitation.sender == state.session or
                invitation.receiver == state.session) and invitation.status == "Accepted":
            accepted = accepted + 1

    return Page(state, menu() + [
        Div(
            Header("Welcome to Campus Connect!"),
            "Plan coffee, study sessions, gym visits, and meals with friends.\n",
            "Currently signed in as: " + state.session,
            classes="hero"
        ),
        Row(
            Div(Header(str(len(state.available_slots[state.session])), 3),
                "Free time slots", classes="stat"),
            Div(Header(str(pending), 3), "Pending invitations", classes="stat"),
            Div(Header(str(accepted), 3), "Accepted plans", classes="stat"),
            classes="stats"
        ),
        Div(
            Header("Switch student", 2),
            "Choose a sample account: ",
            SelectBox("student", STUDENTS, state.session),
            Button("Sign In", "sign_in"),
            classes="panel"
        ),
        Div(
            Header("Get started", 2),
            "Mark your free times on Calendar, compare with a friend, then send an invitation.\n",
            classes="panel"
        )
    ])


@route
def sign_in(state: State, student: str) -> Page:
    """Switch the sample account to the chosen student.

    Parameters:
        state: The information shared by all the pages.
        student: The selected student's name, such as Sam.
    Returns: The Home Page showing the new signed-in student.
    Changes: Updates state.session to the selected name. It does not erase
        anyone's saved free times or invitations.
    """
    state.session = student
    return index(state)


@route
def calendar(state: State) -> Page:
    """Build the clickable weekly schedule for the signed-in student.

    Parameters:
        state: Used to find the student and their saved free times.
    Returns: The Calendar Page with days across the top and times on the
        left. Each button shows whether that time is marked free.
    Changes: Nothing in State. Clicking a button later calls
        toggle_availability to add or remove that time.
    """
    cells = [Div("Time", classes="calendar-corner")]
    for day in DAYS:
        cells.append(Div(day, classes="calendar-day"))

    saved = state.available_slots[state.session]
    for time in TIMES:
        cells.append(Div(time, classes="calendar-time"))
        for day in DAYS:
            slot = day + " at " + time
            if slot in saved:
                label = "Free ✓"
                style = "free-slot"
            else:
                label = "+ Add"
                style = "empty-slot"
            cells.append(Button(label, "toggle_availability",
                                [Argument("day", day), Argument("time", time)],
                                classes=style))

    # *cells "unpacks" the list, passing each cell to Div as its own argument.
    return Page(state, menu() + [
        Header("Weekly Calendar"),
        "Click any time to mark yourself free. Click a green time to remove it.\n",
        "Showing " + state.session + "'s schedule.\n",
        Div(Div(*cells, classes="calendar-grid"),
            classes="table-wrap calendar-scroll panel"),
        "Green = Free     |     Gray = Not marked free\n",
        "Total free times: " + str(len(saved)),
    ])


@route
def toggle_availability(state: State, day: str, time: str) -> Page:
    """Add a free time if it is missing, or remove it if it is saved.

    Parameters:
        state: Holds each student's list of free times.
        day: The clicked day, such as Tuesday.
        time: The clicked time, such as 4 PM.
    Returns: The updated Calendar Page.
    Changes: Calls save_availability or remove_availability, which update
        selected_day and the signed-in student's free times. Invalid days
        or times do not change anything.
    """
    if day not in DAYS or time not in TIMES:
        return calendar(state)
    slot = day + " at " + time
    if slot in state.available_slots[state.session]:
        return remove_availability(state, day, time)
    return save_availability(state, day, time)


@route
def save_availability(state: State, day: str, time: str) -> Page:
    """Save one free-time slot for the signed-in student.

    Parameters:
        state: Holds the signed-in student and all saved schedules.
        day: The day being saved, such as Tuesday.
        time: The time being saved, such as 4 PM.
    Returns: The Calendar Page showing the saved time.
    Changes: Sets state.selected_day and adds the slot to that student's
        list in state.available_slots, but only if it is not already there.
    """
    state.selected_day = day
    slot = day + " at " + time
    if slot not in state.available_slots[state.session]:
        state.available_slots[state.session].append(slot)
    return calendar(state)


@route
def remove_availability(state: State, day: str, time: str) -> Page:
    """Stop marking one time as free for the signed-in student.

    Parameters:
        state: Holds the signed-in student and all saved schedules.
        day: The day to remove, such as Tuesday.
        time: The time to remove, such as 4 PM.
    Returns: The Calendar Page after the change.
    Changes: Sets state.selected_day and removes the slot from that
        student's list if the slot is saved there.
    """
    state.selected_day = day
    slot = day + " at " + time
    if slot in state.available_slots[state.session]:
        state.available_slots[state.session].remove(slot)
    return calendar(state)


@route
def friends(state: State, friend: str = "") -> Page:
    """Compare your free times with another student's free times.

    Parameters:
        state: Holds the current student and everyone's schedules.
        friend: The name to compare with. If blank or invalid, the first
            other sample student is chosen.
    Returns: The Friends Page with a scrolling weekly grid. Green means
        both students are free; blue is you; gold is the friend. It also
        lists shared free times with buttons to suggest an activity.
    Changes: Nothing in State. Comparing schedules only reads the lists.
    """
    others = []
    for student in STUDENTS:
        if student != state.session:
            others.append(student)

    if friend not in others:
        friend = others[0]

    mine = state.available_slots[state.session]
    theirs = state.available_slots[friend]
    cells = [Div("Time", classes="calendar-corner")]
    for day in DAYS:
        cells.append(Div(day, classes="calendar-day"))
    shared = []

    for time in TIMES:
        cells.append(Div(time, classes="calendar-time"))
        for day in DAYS:
            slot = day + " at " + time
            if slot in mine and slot in theirs:
                cells.append(Div("Both free ✓", classes="both-free"))
                shared.append(slot)
            elif slot in mine:
                cells.append(Div("You", classes="you-free"))
            elif slot in theirs:
                cells.append(Div(friend, classes="friend-free"))
            else:
                cells.append(Div("—"))

    lines = [
        Header("Friends & Availability"),
        "Signed in as " + state.session + ". Choose a friend to compare schedules.\n",
        Div(
            "Compare with: ",
            SelectBox("friend", others, friend),
            Button("Compare", "compare_friend"),
            classes="panel"
        ),
        Div(Div(*cells, classes="calendar-grid"),
            classes="table-wrap calendar-scroll panel"),
        "Green = Both free     |     Blue = You     |     Gold = " + friend + "\n",
        Header("Times you are both free", 2),
    ]

    if len(shared) == 0:
        lines.append("No matching free times yet. Add availability to your calendars first.")
    else:
        for slot in shared:
            # split gives two pieces, stored in day and time at the same time.
            day, time = slot.split(" at ")
            lines.append(Div(
                "BOTH FREE: " + slot + "  ",
                Button("Invite " + friend, "suggest", [
                    Argument("friend", friend),
                    Argument("day", day),
                    Argument("time", time),
                ]),
                classes="invite-card"
            ))

    return Page(state, menu() + lines)


@route
def compare_friend(state: State, friend: str) -> Page:
    """Refresh the Friends Page using the friend chosen in the dropdown.

    Parameters:
        state: The existing schedules and signed-in student.
        friend: The selected friend's name, such as Jordan.
    Returns: The Friends Page comparing the two students.
    Changes: Nothing in State. It passes the name to friends.
    """
    return friends(state, friend)


@route
def suggest(state: State, friend: str = "", day: str = "", time: str = "") -> Page:
    """Show the form for choosing and sending an activity invitation.

    Parameters:
        state: Used to find the signed-in student and last selected day.
        friend: Optional friend to fill into the form ahead of time.
        day: Optional day to fill in ahead of time.
        time: Optional time to fill in ahead of time.
    Returns: The Suggest Activity Page with friend, activity, day, and
        time choices. Missing or invalid choices get simple defaults.
    Changes: Nothing in State. Sending happens in send_suggestion.
    """
    other_students = []
    for student in STUDENTS:
        if student != state.session:
            other_students.append(student)

    if friend not in other_students:
        friend = other_students[0]
    if day not in DAYS:
        day = state.selected_day
    if time not in TIMES:
        time = TIMES[0]

    return Page(state, menu() + [
        Header("Suggest Activity"),
        "Pick a friend and activity. Invitations can be sent when you are both free.\n",
        Div(
            "Friend:",
            SelectBox("friend", other_students, friend),
            "\n Activity:",
            SelectBox("activity", ACTIVITIES),
            "\n Day:",
            SelectBox("day", DAYS, day),
            "\n Time:",
            SelectBox("time", TIMES, time),
            "\n",
            Button("Send Invitation", "send_suggestion"),
            classes="panel"
        ),
    ])


@route
def send_suggestion(state: State, friend: str, activity: str,
                    day: str, time: str) -> Page:
    """Try to send an activity invitation to a friend.

    Parameters:
        state: Holds schedules, invitations, and the signed-in student.
        friend: The student being invited.
        activity: The activity choice, such as Coffee or Gym.
        day: The day for the invitation, such as Tuesday.
        time: The time for the invitation, such as 4 PM.
    Returns: A result Page saying whether the invitation was sent and why.
    Changes: Adds one new ActivityInvitation to state.invitations only if
        both students are free and the same invitation was not sent before.
        Otherwise, State stays the same. An existing invitation still
        counts as a duplicate even after it is Accepted or Declined.
    """
    slot = day + " at " + time

    if friend not in STUDENTS or friend == state.session:
        message = "Please choose a different student to invite."
    elif slot not in state.available_slots[state.session]:
        message = "You need to mark yourself free at that time first."
    elif slot not in state.available_slots[friend]:
        message = friend + " has not marked that time as free yet."
    else:
        # Check the main invitation details, even if its status has changed.
        already_sent = False
        for old in state.invitations:
            if (old.sender == state.session and old.receiver == friend and
                    old.activity == activity and old.day == day and old.time == time):
                already_sent = True

        if already_sent:
            message = "You already sent this invitation."
        else:
            state.invitations.append(ActivityInvitation(state.session, friend,
                                                        activity, day, time))
            message = "Invitation sent to " + friend + " for " + activity + "!"

    return Page(state, menu() + [
        Div(
            Header("Invitation Result"),
            message,
            "\n",
            Button("Try Another Activity", "suggest"),
            classes="panel"
        ),
    ])


@route
def inbox(state: State) -> Page:
    """Show all invitations sent to or by the signed-in student.

    Parameters:
        state: Used to look up the student and their invitations.
    Returns: The Inbox Page with received and sent invitations. Pending
        received invitations have Accept and Decline buttons; other
        invitations show their current status.
    Changes: Nothing in State. The response buttons call
        respond_invitation when the student clicks one.
    """
    lines = [Header("Inbox"),
             "Invitations for " + state.session + ".\n",
             Header("Received invitations", 2)]
    received = 0

    # This loop goes through a list of ActivityInvitation dataclass objects.
    # enumerate gives each invitation's position (number) along with it,
    # so the Accept/Decline buttons know which invitation to change.
    for number, invitation in enumerate(state.invitations):
        if invitation.receiver == state.session:
            received = received + 1
            card = [
                Header(invitation.sender + " invited you", 3),
                invitation.activity + " on " + invitation.day +
                " at " + invitation.time + ".\n",
                Div(invitation.status, classes="status " + invitation.status.lower()),
            ]
            if invitation.status == "Pending":
                card.append("\n")
                card.append(Button("Accept", "respond_invitation", [
                    Argument("number", number), Argument("response", "Accepted")
                ]))
                card.append(Button("Decline", "respond_invitation", [
                    Argument("number", number), Argument("response", "Declined")
                ]))
            lines.append(Div(card, classes="invite-card"))

    if received == 0:
        lines.append("You have no received invitations yet.\n")

    lines.append(Header("Sent invitations", 2))
    sent = 0
    for invitation in state.invitations:
        if invitation.sender == state.session:
            sent = sent + 1
            lines.append(Div(
                Header("To " + invitation.receiver, 3),
                invitation.activity + " on " + invitation.day +
                " at " + invitation.time + ".\n",
                Div(invitation.status, classes="status " + invitation.status.lower()),
                classes="invite-card"
            ))

    if sent == 0:
        lines.append("You have no sent invitations yet.\n")

    return Page(state, menu() + lines)


@route
def respond_invitation(state: State, number: int, response: str) -> Page:
    """Accept or decline an invitation from the current student's Inbox.

    Parameters:
        state: Holds the signed-in student and invitation list.
        number: The position of the invitation in state.invitations.
        response: The choice "Accepted" or "Declined".
    Returns: The Inbox Page showing the invitation's current status.
    Changes: Updates that invitation's status only if it exists, belongs
        to the signed-in receiver, and is still Pending. Otherwise it
        does not change State.
    """
    if 0 <= number < len(state.invitations):
        invitation = state.invitations[number]
        if (invitation.receiver == state.session and
                invitation.status == "Pending" and
                response in ["Accepted", "Declined"]):
            invitation.status = response
    return inbox(state)


def new_state() -> State:
    """Make the starting data for a new Campus Connect session.

    Parameters: None.
    Returns: A new State with Alex signed in, Monday selected, empty
        free-time lists for Alex, Sam, and Jordan, and no invitations.
    Changes: Does not change an existing State. It creates a new one.
    """
    return State("Alex", "Monday", {"Alex": [], "Sam": [], "Jordan": []}, [])


def find_grid(page: Page) -> Div:
    """Find the scrolling calendar grid inside a Calendar or Friends Page.

    Parameters:
        page: A Page returned by calendar or friends.
    Returns: The inner calendar-grid Div, or None if it is not found.
    Changes: Nothing. This helper is only used by the tests.

    getattr(block, "extra_settings", {}) safely reads a component's
    settings (like its CSS classes), giving {} if it has none. This was
    not covered in class; it lets the tests look inside page components.
    """
    for block in page.content:
        settings = getattr(block, "extra_settings", {})
        if settings.get("classes") == "table-wrap calendar-scroll panel":
            return block.content[0]
    return None


def run_tests() -> None:
    """Run the simple tests that check whether Campus Connect works.

    Parameters: None.
    Returns: None. The tests print SUCCESS messages in Thonny when they
        pass, or report a failed check if something is wrong.
    Changes: Makes and changes test-only State objects to check sign-in,
        free times, shared availability, invites, and responses. These
        test objects are separate from the real website's starting State.
    """
    state = new_state()

    # The weekly calendar offers hourly choices from 8 AM through 10 PM.
    assert_equal(TIMES[0], "8 AM")
    assert_equal(TIMES[-1], "10 PM")
    assert_equal(len(TIMES), 15)
    long_day = new_state()
    toggle_availability(long_day, "Monday", "8 AM")
    toggle_availability(long_day, "Sunday", "10 PM")
    assert_equal(long_day.available_slots["Alex"],
                 ["Monday at 8 AM", "Sunday at 10 PM"])

    # Check all five pages.
    assert_has(index(state), "Campus Connect")
    assert_has(calendar(state), "Weekly Calendar")
    assert_has(friends(state), "Friends & Availability")
    assert_has(suggest(state), "Suggest Activity")
    assert_has(inbox(state), "Inbox")

    # The calendar grid includes the corner, all seven days, and 15 time rows.
    calendar_grid = find_grid(calendar(state))
    assert_equal(len(calendar_grid.content), 8 * (len(TIMES) + 1))
    assert_equal(calendar_grid.content[0].content[0], "Time")
    assert_equal(calendar_grid.content[7].content[0], "Sunday")
    assert_equal(calendar_grid.content[-8].content[0], "10 PM")
    assert_equal(calendar_grid.content[-1].url, "toggle_availability")

    # Friends uses the same scrolling grid and the same pinned labels.
    friends_grid = find_grid(friends(state))
    assert_equal(len(friends_grid.content), 8 * (len(TIMES) + 1))
    assert_equal(friends_grid.content[0].content[0], "Time")
    assert_equal(friends_grid.content[7].content[0], "Sunday")
    assert_equal(friends_grid.content[-8].content[0], "10 PM")
    assert_equal(friends_grid.content[-1].content[0], "—")

    # Navigation ignores leftover dropdown values from the previous page.
    assert_has(navigate(state, "calendar", student="Sam"), "Weekly Calendar")
    assert_equal(state.session, "Alex")
    assert_has(navigate(state, "index", friend="Jordan"), "Campus Connect")
    assert_has(navigate(state, "inbox", friend="Sam", activity="Food",
                        day="Sunday", time="10 PM"), "Inbox")

    # Check the sign-in and clickable calendar.
    assert_equal(sign_in(state, "Sam").state.session, "Sam")
    toggle_availability(state, "Tuesday", "4 PM")
    assert_equal(state.available_slots["Sam"], ["Tuesday at 4 PM"])
    assert_equal(state.selected_day, "Tuesday")
    save_availability(state, "Tuesday", "4 PM")
    assert_equal(len(state.available_slots["Sam"]), 1)
    toggle_availability(state, "Tuesday", "4 PM")
    assert_equal(state.available_slots["Sam"], [])
    toggle_availability(state, "Tuesday", "4 PM")

    # Both students must be free to invite one another.
    sign_in(state, "Alex")
    assert_has(send_suggestion(state, "Sam", "Coffee", "Tuesday", "4 PM"),
               "mark yourself free")
    save_availability(state, "Tuesday", "4 PM")
    assert_has(friends(state), "BOTH FREE: Tuesday at 4 PM")
    assert_has(compare_friend(state, "Sam"), "BOTH FREE: Tuesday at 4 PM")
    assert_has(suggest(state, "Sam", "Tuesday", "4 PM"), "Send Invitation")

    # An identical invitation must not be added a second time.
    send_suggestion(state, "Sam", "Coffee", "Tuesday", "4 PM")
    assert_equal(len(state.invitations), 1)
    assert_has(send_suggestion(state, "Sam", "Coffee", "Tuesday", "4 PM"),
               "already sent this invitation")
    assert_equal(len(state.invitations), 1)

    # Sam can accept the invitation and Alex can see the new status.
    sign_in(state, "Sam")
    assert_has(inbox(state), "Alex invited you")
    respond_invitation(state, 0, "Accepted")
    assert_equal(state.invitations[0].status, "Accepted")
    respond_invitation(state, 0, "Declined")
    assert_equal(state.invitations[0].status, "Accepted")
    assert_has(inbox(state), "Accepted")
    sign_in(state, "Alex")
    assert_has(inbox(state), "Accepted")
    assert_has(index(state), "Accepted plans")
    assert_has(send_suggestion(state, "Sam", "Coffee", "Tuesday", "4 PM"),
               "already sent this invitation")
    assert_equal(len(state.invitations), 1)

    # Sam can decline a different activity, and cannot respond as Alex.
    send_suggestion(state, "Sam", "Study", "Tuesday", "4 PM")
    respond_invitation(state, 1, "Declined")
    assert_equal(state.invitations[1].status, "Pending")
    sign_in(state, "Sam")
    respond_invitation(state, 1, "Declined")
    assert_equal(state.invitations[1].status, "Declined")
    remove_availability(state, "Tuesday", "4 PM")
    assert_equal(state.available_slots["Sam"], [])


# Run the checks first, then open a clean website with empty schedules.
if __name__ == "__main__":
    run_tests()
    start_server(new_state())
