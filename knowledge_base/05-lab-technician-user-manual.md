# Lab Technician User Manual

This manual is written as a step-by-step recipe. Follow the numbered steps in order. Bold text marks things you click. `Code text` marks the labels of fields you type into.

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Dashboard Tour](#2-dashboard-tour)
3. [Scenario: Viewing all test orders](#3-scenario-viewing-all-test-orders)
4. [Scenario: Opening a test order to view its details](#4-scenario-opening-a-test-order-to-view-its-details)
5. [Scenario: Submitting test results for the first time](#5-scenario-submitting-test-results-for-the-first-time)
6. [Scenario: Updating an existing test report](#6-scenario-updating-an-existing-test-report)
7. [Scenario: Viewing a patient's test history](#7-scenario-viewing-a-patients-test-history)
8. [Common error messages — plain English meaning](#8-common-error-messages--plain-english-meaning)
9. [Tips & gotchas](#9-tips--gotchas)

---

## 1. Getting Started

### 1.1 Logging in

1. Open your web browser (Chrome, Edge, Firefox).
2. Go to the DSI MDR-TB system URL provided by your facility.
3. On the login screen, type your work email into the `Email` field.
4. Type your password into the `Password` field.
5. Click the **Login** button.
6. If your details are correct, the system takes you straight to the **Lab Technician Dashboard**.

### 1.2 What you see right after login

- The page title at the top reads "Dashboard".
- A line near the top reads `Facility Name:` followed by the name of the facility you are assigned to.
- Two coloured cards show your workload counts.
- A table titled **Incoming Tests** lists the most recent test orders waiting for you.
- A left sidebar contains the menu items: **Dashboard**, **Manage Test Orders**, **Settings**, and **Log Out**.

### 1.3 Logging out

1. Look at the bottom of the left sidebar.
2. Click **Log Out**.
3. The system ends your session and returns you to the login page.

### 1.4 Resetting a forgotten password

1. On the login screen, click the **Forgot Password?** link below the password field.
2. Enter your work email address.
3. Click **Send Reset Link**.
4. Open the email that arrives in your inbox.
5. Click the link inside the email.
6. Type a new password twice and click **Reset Password**.
7. Return to the login screen and sign in with the new password.

If the email does not arrive within a few minutes, check your spam folder. If it is still missing, contact your administrator.

---

## 2. Dashboard Tour

The Dashboard is the page you land on after login. It lives at the URL `/lab_technician`.

You can return to it any time by clicking **Dashboard** in the left sidebar.

### 2.1 Facility name line

At the very top, you will see a sentence such as:

> **Facility Name:** Mulago National Referral Hospital

This confirms which facility's tests you are seeing. If this name looks wrong, stop and contact your administrator before processing any tests.

### 2.2 Overview metrics

Below the facility name is a heading that reads **Overview** with a small chart icon. Underneath are two cards:

| Card | What the number means |
|---|---|
| **Pending Tests** | The total number of lab tests at your facility that have been ordered by a doctor but do not yet have results submitted. These are the tests waiting for your action. |
| **Completed Tests** | The total number of lab tests at your facility that have results already submitted. These are tests you (or other technicians) have finished. |

While the dashboard is loading, both cards show grey shimmer placeholders instead of numbers. This is normal — wait a moment for the real numbers to appear.

### 2.3 Incoming Tests list

Below the metrics is a card titled **Incoming Tests** with a beaker icon. It shows the most recent test orders from doctors at your facility.

For each row you will see:

- The patient's name
- The test type (for example, Gene Xpert, Sputum Conversion)
- A status badge
- The date the test was ordered
- Action buttons

If there are no pending tests, you will see an empty-state panel that reads **"No incoming tests"** with the description **"Pending test orders will appear here"**.

To see the complete list (not just the recent ones), click the **See More** button in the top-right of the card. This takes you to the full **Lab Tests** page described in Section 3.

---

## 3. Scenario: Viewing all test orders

**Goal:** See every lab test assigned to your facility, filter by status, and find a specific patient.

### 3.1 Open the page

1. In the left sidebar, click **Manage Test Orders**.
2. The page title becomes "All Test Orders".
3. A card opens with the heading **Lab Tests** and a beaker icon.

(You can also reach this page by clicking the **See More** button on the Dashboard.)

### 3.2 What the table shows

The table has five columns:

| Column | Notes |
|---|---|
| **Patient Name** | First and last name. Click the column header to sort A→Z or Z→A. |
| **Test Type** | Shown as an outlined badge (e.g. "Gene Xpert"). |
| **Status** | A coloured badge — see the meaning below. |
| **Ordered Date** | Formatted as "Mar 15, 2026". Click the header to sort by date. |
| **Actions** | One or two buttons per row, depending on status. |

### 3.3 What each status means clinically

| Status badge | Meaning |
|---|---|
| **ORDERED** (grey badge) | A doctor has requested this test. The specimen has not been processed yet, or the results have not been entered. **This is the queue you work from.** |
| **COMPLETED** (green badge) | Results for this test have already been submitted into the system. The doctor can now review them. You can still open the report to view it or correct it. |
| **CANCELLED** (red badge) | The test order was cancelled and should not be processed. If you see this, do not collect or process a specimen for it. |

### 3.4 Filtering by status

1. Look at the top right of the **Lab Tests** card for a dropdown labelled `Filter by status`.
2. Click the dropdown.
3. Choose one option:
   - **All Statuses** — show every test order (the default).
   - **Ordered** — show only tests that are still waiting for your results.
   - **Completed** — show only tests where results have been submitted.
4. The table updates immediately to match your choice.

To clear the filter, open the dropdown again and pick **All Statuses**.

### 3.5 Searching by patient name

1. Use the search box above the table.
2. Type any part of the patient's first or last name.
3. The table filters live as you type.
4. Clear the box to see all rows again.

### 3.6 Sorting

- Click the **Patient Name** column header to sort patients alphabetically. Click a second time to reverse.
- Click the **Test Type** column header to group tests of the same type together.
- Click the **Ordered Date** column header to put the newest (or oldest) orders at the top.

### 3.7 Mobile view (phone / small screen)

On a phone or narrow window, the table changes into stacked **cards**. Each card shows:

- The patient's name (large, at the top)
- A coloured status badge
- The test type
- The ordered date
- The action buttons (**View Details**, plus **Submit Results** or **Update Report** depending on status)

Scroll up and down to browse cards. Tap a button on a card just like you would click it on a desktop.

---

## 4. Scenario: Opening a test order to view its details

**Goal:** Look at the full information about a single test before deciding what to do.

### 4.1 Click flow

1. In the sidebar, click **Manage Test Orders**.
2. Find the row for the test you want.
3. Click the **View Details** button on the right of the row (or the button at the bottom of the mobile card).
4. The page title changes to "Test Details" and you arrive at a page showing the test name in large letters with a green test-tube icon.
5. To go back, click the **Back** button at the top right.

### 4.2 What the page shows at the top

- The **test name** (e.g. "Gene Xpert"), large and bold.
- A **status badge** matching the colour rules in Section 3.3.
- A **patient badge** showing the patient's name (only if patient data has loaded).
- A green **Report Available** badge if results have already been submitted.

### 4.3 Patient Information section

The first expandable panel is titled **Patient Information**. It opens by default. Inside, you will see four cards:

- `Full Name` — the patient's first and last name.
- `Phone Number` — the patient's contact number, or "Not provided" if none.
- `Gender` — Female or Male.
- `Age` — the patient's age in years, or "Not provided" if missing.

If the patient record has not yet loaded, this section reads "Patient details not available".

### 4.4 Test Order Information section

The second panel is titled **Test Order Information** with a green test-tube icon. It opens by default. It contains:

- `Test Name` — the type of lab test that was ordered.
- `Ordered By` — the name of the doctor who requested the test, prefixed with "Dr.".
- `Ordered At` — the date and time the doctor placed the order. **This time is shown in your computer's local timezone**, so what you see matches the wall-clock time at your facility.
- `Status` — the same coloured badge as on the list page.

### 4.5 Report Details section (only when status is COMPLETED)

If results have already been submitted, a third panel called **Report Details** appears, with a green **Update Report** badge next to the title (clicking it opens the update form — see Section 6).

Inside this panel are four sub-blocks:

1. **Collection Information** (blue block) — `Collection Date`, `Collection Time`, `Collected By`.
2. **Specimen Information** (green block) — `Specimen Type` (badge), `Other Specimen Type` (only if "Other" was chosen), `Volume (mL)`.
3. **Test Results** (purple block) — `Results`, `Observation`, and `Notes` (if entered).
4. **Performance Information** (orange block) — `Performed By` and `Performed At`. The `Performed At` time is shown in your local timezone.

### 4.6 Report Status section (only when status is ORDERED)

If results have not been submitted yet, you will see a panel called **Report Status** with a yellow badge. Clicking the **Submit Report** badge takes you straight into the form described in Section 5.

Inside the panel is the message:

> **Test Results Pending** — This test has been ordered but results are not yet available.

### 4.7 Missing report alert (rare)

If a test is marked COMPLETED but the system cannot find the report data, you will see a red panel titled **Report Status** with a "Missing" badge and the message **"Report Data Not Found"**. Click the **Retry** button inside that panel to reload. If it still does not appear, contact your administrator.

---

## 5. Scenario: Submitting test results for the first time

**Goal:** Record the results of a test that is currently in ORDERED status.

### 5.1 Get to the form

You can reach the **Submit Lab Test Results** form in three ways:

- **From the Dashboard** — find the test in the **Incoming Tests** list and click **Submit Results**.
- **From the test orders list** — go to **Manage Test Orders**, find the row, and click the green **Submit Results** button on the right.
- **From the test details page** — open the test (Section 4), then click the **Submit Report** badge inside the **Report Status** panel.

The page title becomes "Submit Lab Test Results" and a heading at the top reads the same.

### 5.2 Section 1 — Test Order Information (test-tube icon)

Two read-only fields are filled in for you:

- `Lab Test Order ID` — the system ID of the order. Greyed out. Do not edit.
- `Test Name` — the type of test, fetched automatically. Greyed out. Do not edit.

If either field is blank when the page loads, refresh the page once. If it is still blank, go back and re-open the test from the list.

### 5.3 Section 2 — Collection Information (calendar icon)

1. Click into the `Collection Date` field. A date picker opens. Choose the date the specimen was collected. **This field is required.**
2. Look at the `Collection Time` field. The system has already filled it with the current time in HH:MM format. Adjust it if the specimen was collected earlier in the day.
3. Look at the `Collected By` field. The system pre-fills your first name. If a different person actually collected the specimen, clear the field and type their full name. **This field is required.**

### 5.4 Section 3 — Specimen Information (beaker icon)

1. Click the `Specimen Type` dropdown and choose one of:
   - **Sputum**
   - **Blood**
   - **Other**
2. If you chose **Other**, an extra field called `Other Specimen Type` appears. Type a short description of the specimen (for example, "Pleural fluid"). **This field is required when "Other" is selected.**
3. Click into the `Volume (mL)` field and type the volume in millilitres as a number (for example, `5`). **Required.**
4. Click into the `Specimen Appearance` field and type a short visual description (for example, "Clear, mucoid, slightly blood-tinged"). **Required.**

### 5.5 Section 4 — Results and Observations (person icon)

1. Click into the `Results` textarea (4 lines tall) and type the actual lab findings. **Required.**
2. Click into the `Observation` textarea (3 lines tall) and type your professional observations during the test. **Required.**
3. (Optional) Click into the `Notes` textarea and add any extra context — supply lot numbers, equipment used, anything that future readers should know. This field can be left empty.

### 5.6 Save the results

1. Scroll to the bottom of the form.
2. If you want to abandon the form without saving, click **Cancel**. You will be sent back to the test orders page and nothing will be saved.
3. To save, click the blue **Submit Results** button on the right.
4. While the system is saving, the button changes to read **Submitting...** and is disabled. **Do not click it twice.**

### 5.7 What success looks like

- A green toast appears at the top right reading **"Lab test results submitted successfully!"**.
- You are sent back to the **Dashboard**.
- The test no longer appears in the **Pending Tests** count — it is now counted under **Completed Tests**.
- If you go to **Manage Test Orders**, the test's status badge has changed from grey **ORDERED** to green **COMPLETED**, and its action button is now the dark **Update Report** button instead of the green **Submit Results** button.

### 5.8 If saving fails

If the form does not save, a red toast appears with a description such as **"Failed to submit test results"** or **"An error occurred while submitting test results"**. See Section 8 for how to read these messages. Your typed values stay in the form, so you can correct the problem and click **Submit Results** again.

---

## 6. Scenario: Updating an existing test report

**Goal:** Correct or extend a report that has already been submitted.

You can only update reports for tests whose status is **COMPLETED**. If the test is still **ORDERED**, the system will redirect you to the Submit form instead.

### 6.1 Open the update form

You can reach the **Update Test Report** page in two ways:

- **From the test orders list** — find the row with green **COMPLETED** status and click the dark **Update Report** button on the right.
- **From the test details page** — open the test (Section 4) and click the green **Update Report** badge next to the **Report Details** heading.

While the form is loading, you will see a spinner with the message **"Loading test report data..."**. All editable fields are then pre-filled with the values from the existing report.

### 6.2 What you can and cannot edit

| Field | Editable? |
|---|---|
| `Collection Date` | **No** — locked. The description reads "cannot be changed". |
| `Collection Time` | **No** — locked. The description reads "cannot be changed". |
| `Collected By` | Yes |
| `Specimen Type` | Yes |
| `Other Specimen Type` | Yes (only when type is "Other") |
| `Volume (mL)` | Yes |
| `Specimen Appearance` | Yes |
| `Results` | Yes |
| `Observation` | Yes |
| `Notes` | Yes |

### 6.3 Make your changes

1. Click into any editable field and change the value.
2. If you switch `Specimen Type` to or away from **Other**, the `Other Specimen Type` field appears or disappears as needed.
3. Take a moment to re-read the whole form before saving — you cannot undo a save with one click.

### 6.4 Save the update

1. Click **Update Report** at the bottom right.
2. While saving, the button reads **Updating...** and is disabled.
3. On success a green toast appears reading **"Lab test report updated successfully!"** and the system takes you back to the test details page (Section 4), where you can see the new values.
4. If you change your mind before saving, click **Cancel**. You will be sent back to the test orders list with no changes saved.

### 6.5 If the report cannot be found

If, for some reason, the system cannot locate the report attached to the test, you will see a red toast reading **"Cannot find report for this test. Please contact support."** and you will be returned to the test orders list. In that case, ask your administrator for help — do not try to submit a new report on top of the old one.

---

## 7. Scenario: Viewing a patient's test history

**Goal:** See every lab test that belongs to a single patient, in order.

There is no dedicated "patient history" page in the lab technician role, but you can still see a patient's full test history using the test orders list:

1. Click **Manage Test Orders** in the sidebar.
2. In the search box above the table, type the patient's first or last name.
3. The table filters down to only that patient's tests.
4. Click the **Ordered Date** column header to sort the rows. The first click puts the newest tests at the top; click again to put the oldest first. This gives you a chronological view of the patient's testing history.
5. (Optional) Use the `Filter by status` dropdown to narrow further — for example, show only **Completed** tests if you want to see results that have already been entered.
6. Click **View Details** on any row to open the full test record (Section 4) for that particular test.

Repeat for any other patient by clearing the search box and typing a new name.

---

## 8. Common error messages — plain English meaning

When something goes wrong, the system shows a coloured **toast** notification at the top right of the screen. The toasts have a short title and a longer description. Here is what the descriptions actually mean.

### 8.1 "Please check your input"

This title appears with errors that come from the form you just submitted. The description is rewritten into plain English by the system. You will see one of these:

| Description text | What it actually means | What to do |
|---|---|---|
| **"Please check your input and try again."** | A field is invalid but the system could not be more specific. | Re-read every field in the form. Fix anything that looks blank or odd. |
| **"This field is required."** | You left a required box empty. | Find the field flagged in red and fill it in. |
| **"Please enter a valid number."** | You typed letters or a blank in a number field (e.g. `Volume (mL)`). | Type only digits, e.g. `5` or `2.5`. |
| **"Please choose Yes or No for this field."** | A yes/no choice was left unselected. | Click one of the two options. |
| **"A required selection is missing. Please pick an option from the list."** | A dropdown that needs an item was left blank. | Open the dropdown and pick an option. |
| **"Please enter the test name when selecting 'Other'."** | You picked "Other" as the specimen type but did not fill in `Other Specimen Type`. | Type the description of the specimen into the extra field that appeared. |

### 8.2 "Not Found"

| Description text | What it actually means |
|---|---|
| **"The patient record could not be found."** | The patient attached to this test no longer exists in the system. Stop and contact your administrator. |
| **"The selected visit could not be found."** | The visit linked to this test is missing. Contact your administrator. |
| **"No patients are linked to your account yet."** | Your facility has no patients registered. Contact your administrator. |
| **"The requested information could not be found."** | A general "missing record" message. Refresh the page; if it persists, contact your administrator. |

### 8.3 "Network Error"

- **Title:** "Network Error"
- **Description:** "Please check your internet connection and try again."

This means your computer has lost internet access. Check the Wi-Fi or cable, then try the action again. Anything you typed into a form should still be there.

### 8.4 "Access Denied"

- **Title:** "Access Denied"
- **Description:** "You don't have permission to perform this action."

The system thinks you should not be doing this action. You may have been switched to a different role, or your permissions changed. Log out and log back in. If it still happens, contact your administrator.

### 8.5 "Service Unavailable"

- **Title:** "Service Unavailable"
- **Description:** "The service is temporarily unavailable. Please try again later."

The DSI MDR-TB system is offline for maintenance or under heavy load. Wait a few minutes and try again. If it lasts more than 15 minutes, tell your administrator.

### 8.6 "Something went wrong"

- **Title:** "Something went wrong"
- **Description:** "We're having trouble right now. Please try again in a moment."

A general server error. Wait, refresh the page, and try again. If it keeps happening on the same test, note the patient name and test type and contact support.

### 8.7 Account-specific messages

| Description text | Meaning |
|---|---|
| **"Your account isn't fully set up yet. Please contact your administrator."** | The system recognises your login but no profile is attached. Contact your administrator. |
| **"We couldn't load your facility information. Please try again."** | The system could not fetch your facility name on the dashboard. Refresh the page. |

### 8.8 Session expired (silent)

If you have been logged in for a long time without activity, the system may stop responding to actions even though no toast appears. If a button click does nothing and no error toast shows, log out and log back in.

---

## 9. Tips & gotchas

### 9.1 All times are in your local timezone

Wherever you see a date and time on a test details page (`Ordered At`, `Performed At`), the value is converted to your computer's local timezone before being shown. You do **not** need to do timezone math in your head. If your computer's clock or timezone is wrong, ask IT to fix it — otherwise the times you see will not match reality.

### 9.2 Shimmer placeholders mean "still loading"

When you first open the Dashboard or Test Orders page, you may see grey rectangles where text and numbers should be. These are loading placeholders. Wait one or two seconds and the real content will appear. Do not click the same button repeatedly while these are showing.

### 9.3 The "Submitting..." button is disabled on purpose

When you click **Submit Results** or **Update Report**, the button label changes and the button is greyed out. This is to stop you from saving the same data twice. Do not click again — wait for the green success toast or for the page to navigate.

### 9.4 Mobile cards versus desktop tables

On a desktop monitor, test orders appear as a table with rows and columns. On a phone or narrow window, the same data appears as stacked cards instead. The information is the same. The action buttons in the cards do exactly what their column counterparts do.

### 9.5 Empty-state screens

If a page is showing an empty state — for example, **"No incoming tests"** with the description **"Pending test orders will appear here"** — it means there genuinely are no records to show. It is **not** an error. You do not need to refresh.

### 9.6 You can always go back

Every detail page has a **Back** button at the top right. Use it instead of the browser back button — it is more reliable.

### 9.7 Cancel always means "throw away"

The grey **Cancel** button on any form sends you back to the test orders list and saves nothing. Use it only if you genuinely want to discard the form. There is no second confirmation.

### 9.8 You cannot fix locked fields

On the **Update Report** form, `Collection Date` and `Collection Time` are deliberately locked. If those values were entered wrong on the original submission, contact your administrator — there is no way to correct them from the form yourself.

### 9.9 Refresh, then escalate

Most strange behaviour (a missing badge, a stale number on the dashboard, a toast you cannot read) is fixed by refreshing the page once with your browser's reload button. Only contact your administrator if the same problem appears again after a refresh.

---

*For general system navigation, login, and Settings instructions, see the [General System Guide](./00-general-system-guide.md).*
