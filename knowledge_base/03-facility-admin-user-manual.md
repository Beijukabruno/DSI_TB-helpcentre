# Facility Admin User Manual

This manual walks you through the daily tasks of a Facility Administrator on the DSI MDR-TB management web app. Every section is a numbered, click-by-click recipe. Read the section you need and follow the steps in order.

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Dashboard Tour](#2-dashboard-tour)
3. [Scenario: Adding a New Clinician](#3-scenario-adding-a-new-clinician-doctor--nurse--lab-tech--radiologist--radiographer)
4. [Scenario: Viewing All Doctors / Nurses / Lab Techs / Radiologists / Radiographers](#4-scenario-viewing-all-doctors--nurses--lab-techs--radiologists--radiographers-in-your-facility)
5. [Scenario: Updating a Staff Member's Details](#5-scenario-updating-a-staff-members-details)
6. [Scenario: Managing Your Facility Analytics](#6-scenario-managing-your-facility-analytics)
7. [Common Error Messages — Plain English Meaning](#7-common-error-messages--plain-english-meaning)
8. [Tips and Gotchas](#8-tips-and-gotchas)

---

## 1. Getting Started

### 1.1 Logging In

1. Open your browser and go to the DSI MDR-TB web app URL provided by your administrator.
2. You will see a login screen with `Email` and `Password` fields.
3. Type your work email into the `Email` field.
4. Type your password into the `Password` field.
5. Click the **Sign In** button.
6. If your credentials are correct, you will land on the **Facility Dashboard** at the URL `/facility_admin`. The page title in your browser tab will read "Facility Dashboard".

### 1.2 Where You Land

- You only ever see data for **your own facility**. You cannot view staff or patients from other facilities.
- The left sidebar shows three main menu items: **Dashboard**, **Manage Staff**, and **Settings**, plus a **Log Out** option at the bottom.

### 1.3 First-Time Login / Password Reset

1. If this is your first login, the system will force you to change your temporary password before you can access the dashboard. Enter a new password twice and click **Save**.
2. If you forgot your password, click **Forgot Password?** on the login screen, enter your email, and follow the reset link sent to your inbox.

### 1.4 Logging Out

1. Find the **Log Out** item at the bottom of the left sidebar.
2. Click it once.
3. You will be returned to the login screen. Your session is now ended.

---

## 2. Dashboard Tour

**URL:** `/facility_admin` or `/facility_admin/dashboard`

The dashboard is organized into three tabs. Switch between them by clicking the tab labels at the top.

### 2.1 Refreshing the Data

1. Look for the **Refresh Data** button in the top-right corner of the dashboard. It is blue with a circular arrow icon.
2. Click it once.
3. While data reloads, the button label changes to "Refreshing..." and the icon spins.
4. When the spinning stops, all charts and numbers on the page have been updated with the latest figures from the server.

### 2.2 Tab 1 — Overview and Growth

Click the **Overview & Growth** tab (chart-line icon).

- **Facility Overview cards** at the top show four headline numbers for your facility (for example, total staff, total patients, active visits, and new patients in the last 7 days).
- **Patient Growth** line chart — each point on this line is one month. The height of the point is the number of new patients registered that month. If the line slopes up, your facility is registering more patients over time.
- **Staff Growth** line chart — same idea, but for staff members added each month.
- **Yearly Totals** grid — shows cumulative yearly figures (for example, total patients added this year, total staff added this year). Each card has an icon on the left and a number on the right.

If any of these sections is empty, it means there is not yet enough historical data for your facility.

### 2.3 Tab 2 — Clinical and Analytics

Click the **Clinical & Analytics** tab (stethoscope icon).

- **Pending Tests** pie chart — each slice is a type of test currently waiting to be completed (for example, lab tests vs. imaging tests). Hover over a slice to see the exact count. If empty, it reads "No Pending Tests — All tests have been completed".
- **Completed Tests (7 Days)** pie chart — tests finished in the last 7 days, broken down by type. Empty state: "No Completed Tests — No tests have been completed in the last 7 days".
- **Daily Activity** pie chart — everything that happened clinically today, grouped by activity type. Empty state: "No Activity Today".
- **Visits Graph** — daily and weekly patient visit trends. Use the tiny toggle inside the chart to switch between daily and weekly views.
- **Tests Line Graph** — two lines on one chart, one for lab tests and one for imaging tests over time.
- **Prescriptions Line Graph** — number of prescriptions issued per day.

### 2.4 Tab 3 — Patients and Staff

Click the **Patients & Staff** tab (users icon).

- **Facility Patients** panel — shows patient counts and key statistics for your facility.
- **Role Distribution** pie chart — shows the mix of staff by role (Doctor, Nurse, Lab Technician, Radiographer, Radiologist, Facility Admin). Each slice is labelled with the role and the count.

---

## 3. Scenario: Adding a New Clinician (Doctor / Nurse / Lab Tech / Radiologist / Radiographer)

Use this recipe every time you need to create an account for a new staff member.

### 3.1 Click Path

1. From any screen, click **Manage Staff** in the left sidebar. You land on `/facility_admin/manage-staff`.
2. Look at the top-right of the blue header card labelled "Staff Management". You will see a white button with a person-plus icon that reads **Add New Staff**.
3. Click **Add New Staff**.
4. You are taken to the form at `/facility_admin/add-new-staff`. The page heading reads "Add New Staff Member".

### 3.2 Selecting the Role

1. The first field on the form is `Staff Role`, shown as a dropdown. It defaults to **Doctor**.
2. Click the dropdown. You will see six options:
   - Lab Technician
   - Doctor
   - Nurse
   - Facility Admin
   - Radiologist
   - Radiographer
3. Click the role that matches the person you are adding.

### 3.3 Filling the Required Fields

Fill each of the following fields. All four are required.

1. **`Full Name`** — type the person's complete name (for example, "Jane Atuhairwe"). Must be at least 2 characters.
2. **`Phone Number`** — type the phone number. The system accepts numbers starting with `+256`, `+254`, `+250`, `+255`, or a local `0`, followed by `7` and exactly 8 more digits. Example: `+256770430107` or `0770430107`.
3. **`Email Address`** — type a valid work email (for example, `jane.atuhairwe@hospital.org`). It must contain `@` and a domain.

Below the form you will see a blue information box titled "Password Information" that reads:
> "A temporary password will be automatically generated. The user will be prompted to change it on first login."

You do not set a password yourself.

### 3.4 Submitting

1. Click the blue **Create Staff Member** button at the bottom of the form.
2. While the system is saving, the button label changes to "Creating..." and is disabled so you cannot double-click.
3. On success:
   - A green toast appears in the bottom-right that reads **"Staff member created successfully"**.
   - You are redirected back to the Manage Staff page.
   - The new person appears in the Staff Directory table. If they do not appear immediately, click the browser refresh or go back to Manage Staff and reload.

### 3.5 If You Want to Cancel

1. Click the red **Cancel** button next to Create Staff Member.
2. You return to Manage Staff without saving anything.

### 3.6 Error Messages on This Form

| What you see | What it means | What to do |
|---|---|---|
| Red text under a field: "Full name is required" | You left the name blank | Type the full name |
| "Full name must be at least 2 characters" | You typed only one character | Enter at least two characters |
| "Invalid phone number format. Must start with +256, +254, +250, +255, or 0 followed by 9 digits" | Phone number has the wrong shape | Re-enter using one of the accepted prefixes, e.g. `+256770430107` |
| "Please enter a valid email address" | Email is missing `@` or domain | Type a proper email |
| Red toast: "Please check your input" | Server rejected the data (422) | Read the description line in the toast — it tells you which field is wrong |
| Red toast: an email or phone "already exists" | Someone else in the system already has that email/phone | Use a different email/phone |
| Red toast: "Access Denied" | You are not allowed to create this role | Contact a super admin |

---

## 4. Scenario: Viewing All Doctors / Nurses / Lab Techs / Radiologists / Radiographers in Your Facility

You have two ways to view staff: the **combined directory** (all staff in one table) or **role-specific directories** for doctors and lab technicians.

### 4.1 Combined Staff Directory (All Roles)

1. Click **Manage Staff** in the sidebar. You land on `/facility_admin/manage-staff`.
2. Scroll to the white card labelled **Staff Directory**. Next to the title is a blue badge showing how many members are in your facility (for example, "24 members").
3. The table has these columns:
   - **Name** — the person's full name. Clicking it opens their detail page.
   - **Contact** — phone number (truncated with "..." if too long; hover to see the full value).
   - **Email** — email address (truncated; hover to see the full value).
   - **Designation** — role title (Doctor, Nurse, etc.).
   - **Actions** — two buttons per row: an update (pencil) button and a role-management button.

### 4.2 Filtering by Role

1. At the top-right of the Staff Directory card, locate the dropdown labelled **Filter by Role:** (the label is hidden on small screens but the dropdown remains).
2. Click the dropdown. It lists **All Roles** plus every role currently present in your facility.
3. Click the role you want, for example **Nurse**. The table instantly shows only nurses, and the count badge changes to read "4 of 24 members".
4. To see everyone again, click the dropdown and choose **All Roles**.

### 4.3 Sorting and Finding a Person

1. Click the **Name** column header to sort alphabetically. Click again to reverse the order.
2. If the table has many pages, use the pagination controls (**Previous** / **Next** and page numbers) at the bottom of the table.

### 4.4 Role-Specific Lists

Two dedicated pages exist for the largest role groups. They show one role only and can be opened directly by URL:

- **Doctors** — go to `/facility_admin/doctors`. Heading: "Doctor Management". A badge next to "Doctor Directory" shows the total doctor count (for example, "12 doctors").
- **Lab Technicians** — go to `/facility_admin/lab-technicians`. Heading: "Lab Technician Management".

On these pages, clicking a row **expands it in place** to show a details panel with:
- Full name
- ID
- Phone
- Email
- Facility ID
- Created date
- Superuser status (Yes / No)

Click the row again to collapse the details.

For nurses, radiologists, and radiographers, use the combined Staff Directory in section 4.1 with the **Filter by Role** dropdown set to the role you want.

### 4.5 Desktop Tables vs. Mobile Cards

- On a laptop/desktop screen, you see a traditional table with columns.
- On a phone or narrow window, the table automatically switches to **mobile cards** — one card per staff member showing Full Name, Designation, Phone, Email, and the action buttons. This is not a different page; it is the same data in a touch-friendly layout.

### 4.6 Loading and Empty States

- While staff data is loading, you see a **shimmer skeleton** (grey animated bars) instead of rows. Wait a few seconds; do not click repeatedly.
- If you have no staff yet (new facility) the table shows an empty-state illustration with the message that no staff have been added.

---

## 5. Scenario: Updating a Staff Member's Details

Use this recipe when a staff member changes their phone number or name (for example, after marriage).

### 5.1 Getting to the Update Form

There are two paths. Pick whichever is closer to where you are.

**Path A — from the Staff Directory:**

1. Click **Manage Staff** in the sidebar.
2. Find the staff member in the table (use the Filter by Role dropdown or scroll).
3. In their row, click the **Update** button (pencil icon) in the **Actions** column.
4. You are taken to `/facility_admin/update-staff/<their-id>`.

**Path B — from the Staff Details page:**

1. Click **Manage Staff** in the sidebar.
2. Click the staff member's **Name** in the table (it is a blue link).
3. You land on `/facility_admin/staff-details/<their-id>`. You see two cards: "Staff Information" (read-only) and "Actions".
4. In the Actions card, click the **Update Staff Member** button.
5. You are taken to the update form.

### 5.2 What is Editable

Only two fields can be changed on this form:

| Field | Editable? | Rules |
|---|---|---|
| `Full Name` | Yes | Must not be empty |
| `Phone Number` | Yes | Same format rules as Add New Staff (+256/+254/+250/+255 or 0, then 7 and 8 more digits) |
| Email | **No** | Not shown on this form. If an email needs to change, delete the account and create a new one, or escalate to a super admin |
| Role / Designation | **No** | Cannot be changed from this page |

### 5.3 Saving Changes

1. Edit the `Full Name` and/or `Phone Number` field.
2. Click the blue **Update Staff Member** button at the bottom.
3. While saving, the button label changes to "Updating..." and is disabled.
4. On success, a green toast appears reading **"Successfully Updated Staff Member"** and you are returned to the Manage Staff page.
5. If something went wrong, a red toast appears with the message "Failed to update staff member" or a more specific reason. Read section 7 for plain-English meanings.

### 5.4 Cancelling

1. Click the red **Cancel** button next to Update Staff Member.
2. You return to Manage Staff. None of your changes are saved.

### 5.5 Confirming the Update Worked

1. After the success toast, find the staff member in the Staff Directory table.
2. Check that the Contact column shows the new phone number.
3. If you want to see all details, click their name to open the Staff Details page.

---

## 6. Scenario: Managing Your Facility Analytics

The dashboard (section 2) is your everyday analytics view. For a denser, table-heavy analytics page, use the dedicated **Facility Analytics** page.

### 6.1 Opening the Analytics Page

1. In the browser address bar, go to `/facility_admin/analytics` (there is no direct sidebar button; the dashboard covers most daily needs).
2. The page loads several sections stacked vertically.

### 6.2 What Each Section Shows

**Facility Overview**
- Four stat cards: **Total Staff**, **Total Patients**, **Active Visits**, **New Patients (7d)**.
- Below the cards, a **Facility Info** table shows your facility name, location, and the timestamp of when the data was last updated.

**Staff Management Analytics**
- Four stat cards: **Total Staff**, **Doctors**, **Nurses**, **Lab Technicians**.
- A **Recent Staff Additions** list showing names, roles, and creation dates of the most recently added staff.

**Patient Management Analytics**
- Four stat cards: **Total Patients**, **Pending Assignment** (not yet assigned to a doctor), **Recent Registrations**, **Assigned**.
- An **Assignment Coverage** table with detailed assignment statistics.

**Clinical Activity Analytics**
- Four stat cards: **Completed Tests (7d)**, **Pending Tests**, **Daily Activity**, **Pending Lab Tests**.

**Administrative Alerts**
- Four stat cards: **Total Alerts**, **Alert Types**, **Last Checked**, **Items Requiring Action**.
- Below the cards, individual **Alert Cards** each showing a specific alert type, its count, and a sample list of items needing attention.

**Growth and Trends**
- Four stat cards: **Growth Periods**, **Total Patients Added**, **Total Staff Added**, **Yearly Summary Items**.
- A **Yearly Totals** table with year-by-year figures.

### 6.3 Date Filters

This page does not expose a date picker. All windows ("last 7 days", "yearly totals") are calculated server-side. To refresh the figures, go back to the Dashboard (section 2.1) and click **Refresh Data**, or reload the browser tab.

### 6.4 When a Section is Empty

If your facility is new or has no activity, some sections will show zero-value cards or skeleton placeholders. This is normal; data appears as staff and patients start using the system.

---

## 7. Common Error Messages — Plain English Meaning

Toast messages come from the server. The system translates the most common technical messages into friendlier language using `humanizeBackendMessage`. Below is a cheat sheet for the messages you are most likely to see as a facility admin.

| Toast text | Plain English meaning | What to do |
|---|---|---|
| **Network Error** — "Please check your internet connection and try again." | Your browser cannot reach the server | Check your Wi-Fi or mobile data, then retry |
| **Unauthorized** (401) | Your session has expired | Log out and log back in |
| **Access Denied** — "You don't have permission to perform this action." (403) | Your facility admin account is not allowed to do this | Contact a super admin |
| **Not Found** (404) — "The requested information could not be found." | The record you opened no longer exists | Go back to the list and pick another record |
| **Please check your input** (400 or 422) | One or more fields failed validation | Read the description line of the toast; it names the field |
| "This field is required." | A required field was left blank | Fill it in |
| "Please enter a valid number." | You typed letters where a number was expected | Type digits only |
| "Please choose Yes or No for this field." | A Yes/No toggle was left untouched | Pick an option |
| "A required selection is missing. Please pick an option from the list." | A dropdown was left empty | Open it and choose a value |
| "Your account isn't fully set up yet. Please contact your administrator." | The server cannot find a full user record for you | Contact a super admin |
| "We couldn't load your facility information. Please try again." | A temporary failure loading facility details | Click Refresh Data, or reload the page |
| **Something went wrong** (500) — "We're having trouble right now. Please try again in a moment." | Server error, not caused by you | Wait a minute and retry; if it keeps happening, report it |
| **Service Unavailable** (503) | The backend is temporarily down | Wait and retry later |
| **Staff member not found** | You clicked into a staff record that was deleted or does not exist | You are sent back to Manage Staff automatically; try again |
| **Successfully Updated Staff Member** (green) | Your update was saved | No action needed |
| **Staff member created successfully** (green) | The new account was created | No action needed |

---

## 8. Tips and Gotchas

- **Local timezone.** All timestamps (created dates, "last checked", etc.) are shown in your browser's local timezone, not the server's. If you open the app in a different country, times will shift accordingly.
- **Shimmer placeholders.** While data loads, the app shows grey animated "skeleton" bars instead of empty rows. Do not click the same action multiple times — it is loading, not broken.
- **Mobile cards.** On small screens, tables collapse to one-card-per-person. The same Update and Role buttons are inside the card at the bottom.
- **Empty states.** When a list (staff, tests, alerts) has no data, you will see an illustration and a short message. This means "nothing yet", not "error".
- **You only see your facility.** Filters and counts are always scoped to the facility you belong to. You cannot accidentally view or edit another facility's records.
- **Email cannot be edited.** If a staff member mistypes their email at account creation, you cannot fix it from the Update form. Delete the account (from the role-specific page) and re-create it.
- **Role changes.** The Update Staff form does not change a person's role. Use the role action button (**Role** / Assign / Unassign) in the Staff Directory table row to add or remove a role. Assign opens a dropdown of roles not already held by the user; Unassign opens a dropdown of roles currently held.
- **Temporary passwords.** When you create a new staff member, the system generates the password automatically. Tell the person to log in with their email and the temporary password they receive, and to change it on first login.
- **Refreshing data.** The dashboard does not auto-refresh. Click **Refresh Data** (top-right of the dashboard) whenever you want up-to-the-second figures.
- **Double-submit protection.** During any create/update, the submit button disables itself and changes label to "Creating..." or "Updating...". Wait for it to finish; do not click multiple times.

---

*For login, password reset, profile, and general Settings instructions shared across all roles, see the [General System Guide](./00-general-system-guide.md).*
