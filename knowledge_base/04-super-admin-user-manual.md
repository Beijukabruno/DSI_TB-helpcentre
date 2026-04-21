# Super Admin User Manual

This manual is written so a non-technical Super Admin can follow each task like a recipe. Every step is numbered. Click targets appear in **bold**, field labels appear in `code`, and on-screen text is shown in quotes exactly as it appears in the app.

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Dashboard Tour](#2-dashboard-tour)
3. [Scenario: Registering a New Facility](#3-scenario-registering-a-new-facility)
4. [Scenario: Viewing and Updating a Facility](#4-scenario-viewing-and-updating-a-facility)
5. [Scenario: Creating a Facility Admin](#5-scenario-creating-a-facility-admin)
6. [Scenario: Viewing All Facility Admins Across All Facilities](#6-scenario-viewing-all-facility-admins-across-all-facilities)
7. [Scenario: Updating Staff Information](#7-scenario-updating-staff-information)
8. [Scenario: Reading System-Wide Analytics](#8-scenario-reading-system-wide-analytics)
9. [Common Error Messages — Plain English Meaning](#9-common-error-messages--plain-english-meaning)
10. [Tips & Gotchas](#10-tips--gotchas)

---

## 1. Getting Started

### 1.1 Logging In

1. Open your web browser and go to the DSI MDR-TB application URL provided by your IT team.
2. You will land on the login screen.
3. Click inside the `Email` field and type the email address tied to your Super Admin account.
4. Click inside the `Password` field and type your password.
5. Click the **Login** button.
6. If your credentials are correct, the app will route you to the Super Admin landing page at `/super_admin/dashboard`.

### 1.2 The Landing Page

When login completes, the **Dashboard Overview** page loads automatically. You will see:

- A left-hand sidebar with menu items.
- A page header that reads "Dashboard Overview" with the subtitle "System-wide analytics and performance metrics".
- A **Refresh Data** button in the top-right of the dashboard area.
- Three tabs: **Overview & Growth**, **Clinical, Visits & Tests**, and **Users & Facilities**.

### 1.3 Sidebar Navigation

| Menu Item    | Goes to                       |
|--------------|-------------------------------|
| Dashboard    | `/super_admin/dashboard`      |
| Facilities   | `/super_admin/facilities`     |
| Manage Staff | `/super_admin/staff`          |
| Settings     | `/super_admin/settings`       |
| Log Out      | Ends your session             |

### 1.4 Logging Out

1. Locate the sidebar on the left side of any page.
2. Scroll to the bottom of the sidebar.
3. Click **Log Out**.
4. You will be redirected to the login screen and your session will end.

### 1.5 Resetting Your Password

The Super Admin password reset flow is shared with the rest of the system.

1. From the login screen, click the **Forgot Password?** link.
2. Type the email address tied to your account.
3. Click **Send Reset Link**.
4. Open your email inbox and find the message from the system.
5. Click the link in the email — it opens a "Reset Password" page.
6. Type your new password in `New Password`, then again in `Confirm Password`.
7. Click **Reset Password**.
8. You will be returned to the login screen. Sign in with the new password.

If you don't receive the email within a few minutes, check your Spam folder or contact your IT team.

---

## 2. Dashboard Tour

**URL:** `/super_admin/dashboard`

The dashboard is a single page split into a header and three tabs. Data loads automatically when you arrive on the page.

### 2.1 The Page Header

- **Title:** "Dashboard Overview"
- **Subtitle:** "System-wide analytics and performance metrics"
- **Refresh Data button** (top-right): Click it to re-pull every chart from the server. While the request is running, the icon spins and the button label changes to "Refreshing...". When data is loading on first arrival, you will see a series of grey **shimmer** placeholder cards instead of numbers — this is normal.

### 2.2 Tab 1 — Overview & Growth

Click the **Overview & Growth** tab. You will see two charts side by side on wide screens, stacked on small screens:

1. **Growth Over time** (line graph) — Shows how many patients have been registered across all facilities, plotted over each period. The X-axis is the period; the Y-axis is the count of patients registered.
2. **Growth Summary Pie Chart** — A visual breakdown of aggregate growth statistics across the system.

Use this tab when you want to know: "Is the system growing? Are more patients being registered over time?"

### 2.3 Tab 2 — Clinical, Visits & Tests

Click the **Clinical, Visits & Tests** tab. You will see:

1. **Clinical Throughput** card at the top with four metric tiles:
   - `Active Visits` — visits currently open in the system.
   - `Completed Visits in the last 24hrs` — visits closed in the past day.
   - Two further tiles showing additional throughput numbers (e.g. lab tests and prescriptions for the period).
   A small pulsing dot on the Active Visits tile means the number is live.
2. **Visit Trends Line Graph** — Toggle between daily and weekly aggregates of patient visits across all facilities.
3. **Tests Line Graph** — Lab tests and imaging tests trends over time, plotted on the same chart for comparison.
4. **Prescriptions Line Graph** — Daily prescription volume across the system.

Use this tab when you want to know: "How busy are the clinics today? Are tests and prescriptions being recorded?"

### 2.4 Tab 3 — Users & Facilities

Click the **Users & Facilities** tab. You will see:

1. **Role Distribution Pie Chart** — A breakdown of all staff in the system by role: Doctor, Nurse, Lab Technician, Radiographer, Radiologist, and Facility Admin. Hover over a slice to see the exact count.
2. **Facilities Coverage** card with three summary tiles:
   - `Total Facilities` — every facility currently registered.
   - A tile showing facilities that have an admin assigned.
   - `Average staff per facility` — the mean number of staff across all facilities.
   Below the tiles is a list of every facility. Click a facility row to expand it and see its individual staff numbers and admin assignment status.

Use this tab when you want to know: "Which facilities still need an admin? How is staff distributed across the network?"

### 2.5 Refreshing the Dashboard

1. Click the **Refresh Data** button in the top-right.
2. The icon spins and the label changes to "Refreshing...".
3. When the spinner stops, every chart on every tab now reflects the latest server data.

---

## 3. Scenario: Registering a New Facility

Goal: Add a brand-new clinic to the system so patients and staff can be linked to it.

### 3.1 Navigate to the Facilities Page

1. In the left sidebar, click **Facilities**.
2. The page at `/super_admin/facilities` opens, showing a table (desktop) or a stack of cards (mobile) of all existing facilities.

### 3.2 Open the Add Facility Form

1. At the top of the Facilities page, click the **Add** button.
2. A dialog opens (or, if you reach the page directly, the route `/super_admin/add-new-facility` loads). The header reads: "Fill in the details below to register a new facility. Fields marked with * are required."

### 3.3 Fill in the Form

Every field marked with a red `*` is required. The four location fields are **cascading** — each one unlocks the next.

1. Click in `Facility Name` and type the official name of the clinic (e.g. "Mulago National Referral Hospital"). The placeholder text is "Enter facility name".
2. Click the `District` dropdown. The list shows every district in Uganda. Select the district where the facility is located.
3. Once a district is chosen, the `Sub County` dropdown becomes active. Click it and select the sub-county.
4. Once a sub-county is chosen, the `Parish` dropdown becomes active. Click it and select the parish.
5. Once a parish is chosen, the `Village` dropdown becomes active. Click it and select the village.

If you change a higher-level field (for example, you switch the district), the lower fields (sub-county, parish, village) are automatically cleared. You will need to re-select them.

### 3.4 Submit the Form

1. Verify every field is filled in.
2. Click the blue **Add Facility** button (left button at the bottom). While the request is running, the label changes to "Submitting...".
3. On success, a green toast appears at the top of the screen reading **"Successfully Added new Facility"**, the form clears, and you are redirected back to the Facilities list.
4. If anything goes wrong, a red toast appears reading **"Failed to register facility"** with a description of the cause.

To abandon the form, click the red **Cancel** button. You will return to the Facilities page and no facility will be created.

### 3.5 Field-Level Errors and What They Mean

| Error message under a field      | What it means                                                                |
|----------------------------------|------------------------------------------------------------------------------|
| "name is required"               | You did not type a facility name.                                            |
| "district is required"           | You did not pick a district from the dropdown.                               |
| "sub county is required"         | You did not pick a sub-county.                                               |
| "parish is required"             | You did not pick a parish.                                                   |
| "village is required"            | You did not pick a village.                                                  |
| Toast: "Failed to register facility" | The server rejected the request. The toast description tells you why. See section 9. |

---

## 4. Scenario: Viewing and Updating a Facility

Goal: Find an existing facility and change its name or location data.

### 4.1 Locate the Facility

1. In the left sidebar, click **Facilities**.
2. The Facilities page opens. On desktop you see a table with columns: `Facility Name`, `District`, `Parish`, `Sub County`, `Village`, and `Action`. On mobile you see a card per facility.
3. The table shows 10 facilities per page. The footer reads "Showing 1 to 10 of N entries".
4. To move between pages, click a page number in the **PaginationTabs** control on the bottom-right.
5. Scan the list for the facility you want. You can also use your browser's Find feature (Ctrl+F or Cmd+F) to search the visible page.

### 4.2 Open the Facility Details Page

1. Click the **facility name** in the first column (it is underlined on hover and acts as a link).
2. The Facility Details page at `/super_admin/facility-details/{facilityId}` opens. The header shows the facility name and the subtitle "Facility Details and Management".
3. The **Facility Information** card displays five read-only fields: `Facility Name`, `District`, `Sub County`, `Parish`, `Village`.
4. To go back without changing anything, click the **← Back to Facilities** button in the top-right.

### 4.3 Edit the Facility

You can reach the edit form in two ways:

- **From the table:** click the **Update** button in the Action column of the row.
- **From the details page:** click the **Update Facility** button in the Actions card.

Both routes take you to `/super_admin/update-facility/{facilityId}`. The header reads "Update Facility" and the subtitle reads "Update the facility details below. Fields marked with * are required." All five fields are pre-filled with the facility's current values.

1. To rename the facility, click in `Facility Name` and type the new name.
2. To change the location, change the `District` first. This will reset and disable `Sub County`, `Parish`, and `Village`. Re-select each one in order.
3. If you only need to change a lower level (e.g., a different `Village` in the same parish), use only that dropdown.

### 4.4 Save the Changes

1. Review every field one more time.
2. Click the blue **Update Facility** button. While the request is running the label changes to "Updating...".
3. On success a green toast reads **"Successfully Updated Facility"** and you return to the Facilities list.
4. On failure a red toast reads **"Failed to update facility"** with a description.
5. To abandon your changes, click the red **Cancel** button.

---

## 5. Scenario: Creating a Facility Admin

Goal: Add a new Facility Admin user and link them to a specific facility so they can manage that clinic's day-to-day staff.

### 5.1 Navigate to Manage Staff

1. In the left sidebar, click **Manage Staff**.
2. The page at `/super_admin/staff` opens. The header is "Facility Admin".

### 5.2 Open the Add Form

1. Click the **Add** button at the top of the page.
2. The route `/super_admin/add-new-staff` loads. The header reads "Add New Facility Admin" with the subtitle "Create a new facility administrator account".
3. Below the header is a card titled "Administrator Details" containing the form.

### 5.3 Fill in the Form

There are four required fields. Every field shows a red `*` next to its label.

1. **`Facility` (dropdown).** Click it. The list contains every facility you have registered. Select the facility this admin will manage. The validation message if you skip this is "Select a facility".
2. **`Full Name` (text).** Type the admin's complete legal name. The placeholder is "Enter full name". The validation message if blank is "Provide Admin full names".
3. **`Phone Number` (phone input).** Type the admin's mobile number. Accepted formats are:
   - Uganda: `+256` or `0` followed by `7` and 8 digits (e.g. `+256770430107` or `0770430107`).
   - Kenya: `+254` followed by `7` and 8 digits.
   - Rwanda: `+250` followed by `7` and 8 digits.
   - Tanzania: `+255` followed by `7` and 8 digits.
   The validation message for an invalid format is "Invalid phone number format. Must start with +256, +254, +250, +255, or 0 followed by 9 digits".
4. **`Email Address` (email).** Type the admin's email. The placeholder is "Enter email address". The validation message if blank is "Email is required".

### 5.4 Submit the Form

1. Click the blue **Create Facility Admin** button. While the request is running, the label changes to "Creating…".
2. On success, a green box appears above the form reading **"Created successfully."** The form clears so you can add another admin if needed.
3. The new admin is created with a temporary password (`defaultPassword123`). Share the temporary password with the new admin via a secure channel. They will be prompted to change it on first login.
4. To return to the staff list without saving, click the red **Cancel** button.

### 5.5 What Success Looks Like

- The green "Created successfully." box is visible above the form.
- When you navigate back to **Manage Staff**, the new admin appears in the table with their name, email, phone, and the facility you assigned.
- The **Facilities Coverage** card on the dashboard will show one fewer facility without an admin (after you click **Refresh Data**).

### 5.6 Errors

| Where it appears                       | Message                                              | Meaning                                         |
|----------------------------------------|------------------------------------------------------|-------------------------------------------------|
| Below `Facility`                       | "Select a facility"                                  | You did not pick a facility from the dropdown.  |
| Below `Full Name`                      | "Provide Admin full names"                           | The full name field is empty.                   |
| Below `Phone Number`                   | "Phone Number required"                              | The phone field is empty.                       |
| Below `Phone Number`                   | "Invalid phone number format..."                     | The number you typed is not in an accepted format. |
| Below `Phone Number` (after submit)    | "Invalid Phone Format"                               | The server rejected the phone number.           |
| Below `Email Address`                  | "Email is required"                                  | The email field is empty.                       |
| Red box above the form                 | (server message)                                     | A network or server error occurred.             |

---

## 6. Scenario: Viewing All Facility Admins Across All Facilities

Goal: See a single, system-wide list of every Facility Admin, regardless of which clinic they belong to.

### 6.1 Open the Page

1. In the left sidebar, click **Manage Staff**.
2. The page at `/super_admin/staff` loads.

### 6.2 Read the Desktop Table

On wide screens (laptop / desktop), the table has these columns:

| Column     | What it shows                                                          |
|------------|------------------------------------------------------------------------|
| `Name`     | The admin's full name. Click to open Staff Details.                    |
| `Email`    | The admin's email address.                                             |
| `Phone`    | The admin's contact phone number.                                      |
| `Facility` | The name of the facility this admin manages.                           |
| `Action`   | Two icon buttons: **Update** and **Delete**.                           |

The table shows 10 admins per page. The footer reads "Showing 1 to 10 of N entries". Use the page numbers in **PaginationTabs** at the bottom-right to move between pages.

### 6.3 Read the Mobile Cards

On phones and narrow screens, each admin is shown as a card:

- The card header shows the admin's **name** (large) and **email** (small).
- A divider separates the header from the details.
- Below the divider you see `Phone` and `Facility`.
- In the top-right of each card are two icon buttons: **Update** and **Delete**.

Tap the body of a card to open Staff Details.

### 6.4 Filtering and Searching

The Manage Staff list does not have a built-in search box or filters. To find a specific admin:

1. Use **PaginationTabs** to flip through pages.
2. Or use your browser's Find feature (Ctrl+F on Windows / Cmd+F on Mac) to search the visible text on the current page.
3. Or sort visually by `Facility` to group admins by clinic.

### 6.5 Open an Admin's Details

1. Click anywhere on the row (desktop) or card body (mobile) of the admin you want to inspect.
2. The Staff Details page at `/super_admin/staff-details/{staffId}` opens.
3. The header shows the admin's full name and the subtitle "Staff Member Details and Management".
4. The **Staff Information** card lists `Full Name`, `Email`, `Phone Number`, and `Assigned Facility`.
5. The **Assigned Facility Information** card lists `Facility Name`, `District`, `Sub County`, `Parish`, and `Village` of the facility this admin runs.
6. To go back, click the **← Back to Staff** button in the top-right.

---

## 7. Scenario: Updating Staff Information

Goal: Correct an admin's name or phone number.

### 7.1 Reach the Edit Form

You can open the edit form in two ways:

- **From the staff table or card:** click the **Update** icon button in the row's Action area.
- **From the staff details page:** click the **Update Staff Member** button in the Actions card.

Both routes take you to `/super_admin/update-staff/{staffId}`. The form is in a card titled "Details".

### 7.2 What Is Editable

Only two fields can be changed from this page:

| Field          | Editable | Notes                                                       |
|----------------|----------|-------------------------------------------------------------|
| `Full Name`    | Yes      | Required. Cannot be left blank.                             |
| `Phone Number` | Yes      | Required. Same format rules as section 5.3.                 |
| Email          | No       | Email is fixed. Contact IT if it must change.               |
| Facility       | No       | The facility assignment cannot be changed from this screen. |

### 7.3 Save the Changes

1. Click in `Full Name` and edit if needed.
2. Click in `Phone Number` and edit if needed.
3. Click the blue **Update Staff Member** button. While the request is running, the label changes to "Updating...".
4. On success a green toast reads **"Successfully Updated Staff Member"** and you return to the staff list.
5. On failure a red toast reads **"Failed to update staff member"** with a description.
6. To abandon, click the red **Cancel** button.

If you typed a bad phone number, the field will turn red and show the message "Invalid Phone Format" after you submit.

### 7.4 Deleting a Staff Member

1. Open the Staff Details page for the admin you want to remove.
2. Scroll to the **Actions** card at the bottom.
3. Read the yellow warning box: "Deleting a staff member will permanently remove them from the system. This action cannot be undone."
4. Click the red **Delete Staff Member** button.
5. A confirmation dialog opens with the title **"Press Continue to Delete Facility Admin"** and the description "This action cannot be undone. The facility admin will be permanently removed."
6. To back out, click the grey **Cancel** button.
7. To proceed, click the red **Continue** button.
8. On success a green toast reads **"Successfully Deleted Staff Member"** and you are returned to the staff list.
9. On failure a red toast reads **"Failed to delete staff member"** with the cause.

You can also click the **Delete** icon button directly from the staff table or mobile card without going into details first; the same confirmation dialog will appear.

---

## 8. Scenario: Reading System-Wide Analytics

Goal: Understand what each chart on the dashboard is telling you so you can make decisions about staffing, supplies, and rollout.

### 8.1 Growth Over time (Tab 1)

- **What it shows:** the number of patients newly registered in the system, broken down by period (e.g. day, week, month depending on the data).
- **How to read it:** the X-axis is time; the Y-axis is the patient count. A rising line means the system is gaining patients; a flat line means registration has stalled.
- **Use it for:** spotting growth trends, judging the impact of an outreach campaign, or noticing when a region has gone quiet.

### 8.2 Growth Summary Pie Chart (Tab 1)

- **What it shows:** the aggregate composition of patient growth (e.g. categories of registrations rolled together).
- **How to read it:** each slice is a category; the size is the percentage of the total.
- **Use it for:** at-a-glance composition checks.

### 8.3 Clinical Throughput (Tab 2)

- **Active Visits:** how many patient visits are currently open right now. The pulsing dot signals that this is a live count.
- **Completed Visits in the last 24hrs:** how many visits were closed in the past day. Use this as a daily productivity number.
- **Other tiles:** show recent lab and prescription volumes; a high number with a low Active Visits number means staff are processing visits quickly.
- **Use it for:** confirming the system is being used today, not just historically.

### 8.4 Visit Trends Line Graph (Tab 2)

- **What it shows:** total visits per day or per week. There is usually a toggle so you can switch between daily and weekly views.
- **How to read it:** spikes mean unusually busy days; troughs mean quiet days. Compare weekday vs weekend patterns.
- **Use it for:** scheduling staff, planning supply deliveries.

### 8.5 Tests Line Graph (Tab 2)

- **What it shows:** lab tests and imaging tests plotted on the same time axis.
- **How to read it:** if lab tests rise but imaging stays flat, your bottleneck might be in the imaging room; if both fall, the clinic is generally quiet.
- **Use it for:** identifying which clinical service is over- or under-used.

### 8.6 Prescriptions Line Graph (Tab 2)

- **What it shows:** how many prescriptions are issued each day across the system.
- **How to read it:** prescription volume tracks visit volume in a healthy clinic. If visits are high but prescriptions are low, doctors may be skipping the system.
- **Use it for:** auditing whether providers are completing the prescription step.

### 8.7 Role Distribution Pie Chart (Tab 3)

- **What it shows:** the share of staff in each role (Doctor, Nurse, Lab Technician, Radiographer, Radiologist, Facility Admin) across the entire system.
- **How to read it:** hover a slice to see the exact count and percentage.
- **Use it for:** spotting role imbalance — for example, too few lab technicians for the test volume you saw on tab 2.

### 8.8 Facilities Coverage (Tab 3)

- **Total Facilities:** every facility currently in the system.
- **Facilities with admin:** facilities that have a Facility Admin assigned.
- **Average staff per facility:** the mean number of clinical staff across all facilities.
- **Facility list:** click any row to expand and see that facility's individual coverage details.
- **Use it for:** finding facilities that still need an admin (handle by following section 5).

---

## 9. Common Error Messages — Plain English Meaning

The system rewrites raw backend errors using a helper called `humanizeBackendMessage`. The table below maps the rewritten messages you may see in red toasts to their plain meaning and your next step.

| Toast title                  | Toast description (humanised)                                                | What it really means                                                                              | What to do                                                                                  |
|------------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| "Network Error"              | "Please check your internet connection and try again."                       | The browser is offline, or the server is unreachable.                                             | Check your Wi-Fi or wired connection, then click the action again.                          |
| "Please check your input"    | "This field is required."                                                    | A required field was left blank.                                                                  | Find the empty field and fill it in.                                                        |
| "Please check your input"    | "A required selection is missing. Please pick an option from the list."      | A dropdown was left at "Select…".                                                                 | Open the dropdown and choose a value.                                                       |
| "Please check your input"    | "Please choose Yes or No for this field."                                    | A Yes/No field was sent in the wrong shape.                                                       | Re-tick the toggle and try again.                                                           |
| "Please check your input"    | "Please enter a valid number."                                               | A number field had non-numeric content.                                                           | Replace letters or symbols with digits.                                                     |
| "Not Found"                  | "We couldn't load your facility information. Please try again."              | The server could not retrieve the facility record.                                                | Click **Refresh Data** or try again in a moment. If it persists, contact IT.                |
| "Not Found"                  | "The requested information could not be found."                              | The page tried to fetch a record (facility, user) that no longer exists.                          | Go back to the list and pick a current item.                                                |
| "Not Found"                  | "Your account isn't fully set up yet. Please contact your administrator."   | The server says "User not found" for the logged-in account.                                       | Contact IT — your profile is incomplete.                                                    |
| "Access Denied"              | "You don't have permission to perform this action."                          | Your account is not authorised for this action even though you reached the page.                  | Confirm you are logged in as Super Admin. If yes, contact IT.                               |
| "Something went wrong"       | "We're having trouble right now. Please try again in a moment."              | A server-side error (HTTP 500). Not your fault.                                                   | Wait a minute, then retry. If it keeps failing, contact IT.                                 |
| "Service Unavailable"        | "The service is temporarily unavailable. Please try again later."            | The backend is restarting or in maintenance.                                                      | Try again in a few minutes.                                                                 |
| "Failed to register facility"| (server message)                                                             | The Add Facility request was rejected.                                                            | Read the description, fix the named field, resubmit.                                        |
| "Failed to update facility"  | (server message)                                                             | The Update Facility request was rejected.                                                         | Read the description, fix the named field, resubmit.                                        |
| "Failed to delete staff member" | (server message)                                                           | The Delete request was rejected.                                                                  | Read the description. May indicate the user is already deleted — refresh the list.          |
| "Failed to update staff member" | (server message)                                                           | The Update Staff request was rejected.                                                            | Read the description and correct the offending field.                                       |
| "Unauthorized"               | (silent — session ended)                                                     | Your login has expired.                                                                           | Refresh the page; you will be sent to the login screen. Sign in again.                      |

If you ever see a red toast whose description is not in this table, the helper will at least capitalise the first letter and end it with a period — read it literally; it usually names the field that was wrong.

---

## 10. Tips & Gotchas

### 10.1 Local Time Zone

All times shown on the dashboard (Active Visits, Completed Visits in the last 24hrs, Visit Trends, etc.) are computed against the server's notion of "now". If you are working from a different time zone than the server, the "last 24 hours" window may not match your local clock exactly.

### 10.2 Loading Shimmer

When the dashboard first loads — and after you click **Refresh Data** — you will briefly see grey rectangular **shimmer** placeholders where the cards and charts will appear. This is expected. Do not click anything until the shimmer disappears, otherwise you may trigger duplicate requests.

### 10.3 Mobile Cards vs Desktop Tables

The Facilities and Manage Staff pages automatically switch between a wide table on laptops and a stack of cards on phones. The data is identical; only the layout changes. On mobile, action buttons (**Update**, **Delete**) live in the top-right of each card.

### 10.4 Empty States

If you arrive at the Facilities or Manage Staff page and the list is empty, no error is shown — the table simply has no rows, and the footer reads "Showing 1 to 0 of 0 entries". This means no records exist yet. Use the **Add** button to create your first record.

### 10.5 Cascading Dropdowns Reset Lower Levels

Whenever you change `District`, the `Sub County`, `Parish`, and `Village` selections are wiped. The same chain effect happens at every level. Always work top-down through the four location fields.

### 10.6 Pagination Resets When You Navigate Away

The Facilities and Manage Staff pages always start on page 1 when you arrive. If you were on page 4 and navigated to a details page and back, you will need to flip to page 4 again.

### 10.7 Default Password for New Admins

Newly-created Facility Admins are set up with a temporary password (`defaultPassword123`). Always remind the new admin to change this on their first login. Treat the temporary password as sensitive and share it through a secure channel.

### 10.8 Cancel Means Cancel

The red **Cancel** button on every form discards all the values you typed. There is no autosave. If you accidentally click it, you will need to retype the form.

### 10.9 You Cannot Reassign a Facility Admin

The Update Staff form does not allow changing the `Facility` linked to an admin. If a person needs to move from Facility A to Facility B, **delete** the admin from Facility A and **create** a new admin record under Facility B (sections 7.4 and 5).

### 10.10 Refresh Versus Reload

The **Refresh Data** button only refreshes the dashboard data; it does not reload the page itself. If a chart looks stuck or broken, try a full browser reload (F5 or Ctrl+R) before contacting IT.

---

*For login screens, profile settings, and shared navigation that applies to every role, see the [General System Guide](./00-general-system-guide.md).*
