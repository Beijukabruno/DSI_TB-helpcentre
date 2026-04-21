# Radiologist User Manual

A step-by-step guide for radiologists using the DSI MDR-TB management web app. Each section is self-contained — skip to the scenario you need.

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Dashboard Tour](#2-dashboard-tour)
3. [Scenario: Viewing All Imaging Tests Requiring Review](#3-scenario-viewing-all-imaging-tests-requiring-review)
4. [Scenario: Opening a Test for Review](#4-scenario-opening-a-test-for-review)
5. [Scenario: Viewing Uploaded Medical Images](#5-scenario-viewing-uploaded-medical-images)
6. [Scenario: Submitting a Radiology Report](#6-scenario-submitting-a-radiology-report)
7. [Scenario: Editing a Previously Submitted Report](#7-scenario-editing-a-previously-submitted-report)
8. [Scenario: Viewing a Patient's Imaging History](#8-scenario-viewing-a-patients-imaging-history)
9. [Common Error Messages — Plain English Meaning](#9-common-error-messages--plain-english-meaning)
10. [Tips & Gotchas](#10-tips--gotchas)

---

## 1. Getting Started

### 1.1 Logging in

1. Open your browser and go to the DSI MDR-TB application URL provided by your administrator.
2. On the login page, type your email into the **Email** field.
3. Type your password into the **Password** field.
4. Click the **Login** button.
5. If your credentials are correct, the app takes you straight to the Radiologist Dashboard at `/radiologist`.

### 1.2 The landing page

After login you land on the **Dashboard**. You will see:

- A left-hand sidebar with **Dashboard**, **Imaging Tests**, **Settings**, and **Log Out**.
- A top bar showing the current page title (e.g. `Dashboard`).
- Three metric cards at the top of the main area.
- A **Pending Reports** card.
- A **Recent Reports** card.

### 1.3 Resetting a forgotten password

1. On the login page, click the **Forgot Password?** link.
2. Type your registered email into the field.
3. Click **Send Reset Link**.
4. Open the email inbox for that address and click the link in the email.
5. Enter a new password twice and click **Reset Password**.
6. Return to the login page and sign in with the new password.

If the email never arrives, contact your system administrator. Do not create a second account.

### 1.4 Logging out

1. In the left sidebar, click **Log Out** (bottom of the menu).
2. The app ends your session and returns you to the login page.

Always log out when you leave a shared workstation.

---

## 2. Dashboard Tour

**URL:** `/radiologist`

The dashboard has three sections: Overview metrics, Pending Reports, and Recent Reports.

### 2.1 Overview metric cards

At the top of the dashboard are three colored cards. Each card shows a number pulled from the `/radiologist/stats` endpoint.

| Card | What the number means |
|---|---|
| **Total Reports Created** (blue left border) | The total count of radiology reports you have ever submitted on this system. It does not reset. |
| **Pending** (yellow left border) | The number of imaging tests that have been uploaded by a radiographer and are waiting for a radiologist to read and report. This is your inbox. |
| **Reports Today** (red left border) | The number of reports you personally submitted since midnight today (server local time). Use this to track your daily output. |

If the cards show shimmer placeholders (grey blinking rectangles), the stats are still loading — give it a second.

### 2.2 Pending Reports card

Below the metrics is a card headed **Pending Reports** with a pill showing the count (e.g. `7 reports`).

- It lists up to 3 of the most recent tests awaiting your analysis.
- On desktop it is a table with columns **Patient**, **Body Part**, **Reported**, **Actions**.
- On mobile each row becomes a stacked card with the same labels in bold.
- The **Reported** column shows a relative time (e.g. `2 hours ago`) based on when the radiographer performed the test.
- The **View** button in the Actions column opens the test details page.
- If there are no pending tests, the card shows an empty state: `No pending reports` with the sub-text `Tests awaiting reports will appear here`.

To see more than the top 3, go to **Imaging Tests** in the sidebar (see Section 3).

### 2.3 Recent Reports card

The bottom card is headed **Recent Reports** with a pill showing how many reports you have.

- It lists up to 3 of your most recent submitted reports.
- Columns: **Patient**, **Finding**, **Reported**, **Actions**.
- **Finding** shows the `extent_of_disease` value you selected (e.g. `moderately advanced disease`).
- **Reported** shows how long ago you submitted the report.
- **View** opens that report's details page where you can edit it.
- If you have never submitted a report, the card shows `No reports found` with the sub-text `Created reports will appear here`.

---

## 3. Scenario: Viewing All Imaging Tests Requiring Review

**Goal:** See every imaging test — both awaiting your review and already reported.

**URL:** `/radiologist/imaging_tests`

### 3.1 Opening the list

1. In the left sidebar, click **Imaging Tests**.
2. The page header reads **Reports** with a count pill showing the total number of items (pending + completed combined).

### 3.2 What the table shows

The list merges two things:

- **Pending tests** (status `PENDING`, meaning the radiographer uploaded images and nobody has reported yet).
- **Your completed reports** (status `COMPLETED`, previously called `ANALYZED`).

Desktop columns:

| Column | Meaning |
|---|---|
| **Patient** | The patient's full name. |
| **Finding** | For completed reports, the `extent_of_disease` you recorded. For pending tests, this cell shows `Pending`. |
| **Time** | For completed reports, the reported-at timestamp as relative time. For pending tests, the performed-at timestamp. |
| **Actions** | A **View** button, and for PENDING rows an additional green **Submit Report** button. |

On mobile, each row becomes a card with the same four fields stacked, labels in bold.

### 3.3 Understanding the status indicators

There are only two states you will encounter as a radiologist:

- **PENDING / Awaiting Analysis** — the radiographer has uploaded the images. No report exists yet. It is waiting for you. The status badge appears yellow on the details page.
- **COMPLETED / ANALYZED** — a radiology report has been submitted. The status badge appears green on the details page. The ordering doctor can now see your findings.

On this list page the status itself is not shown as a colored badge; you infer it from the **Finding** column (it says `Pending` for unreviewed tests) and from the presence of the green **Submit Report** button.

### 3.4 Searching

1. Click the search box labeled **Search test type or status...** at the top-right of the Reports card.
2. Type part of a patient name.
3. The table filters live as you type. Clear the box to see everything again.

Note: despite the placeholder wording, the search actually matches against the patient name.

### 3.5 Taking action

- To review a pending test: click the green **Submit Report** button on that row. It opens the test details page with the report form ready.
- To review or edit an already-reported test: click **View** on a completed row.
- To just open any row regardless of status: click **View**.

---

## 4. Scenario: Opening a Test for Review

**Goal:** Open one specific imaging test and see everything about it.

**URL:** `/radiologist/imaging_test/:id`

### 4.1 Getting to the details page

From the Dashboard:

1. In the **Pending Reports** card, find the row for the patient.
2. Click **View** in the Actions column.

From the Imaging Tests list:

1. Sidebar → **Imaging Tests**.
2. Find the row and click **View** (or **Submit Report** for a pending test).

If the test ID is invalid or missing, you will see a red box titled **Test Not Found** with the sub-text `The imaging test with ID {id} could not be found.` In that case, click the browser Back button and reopen the row.

### 4.2 What you see at the top

A dark blue header bar contains:

- The **patient's name** in large white text.
- A line below with the body part and the performed date (e.g. `Chest · 10/14/2024`).
- On the right, a **status badge**:
  - Yellow badge reading `Awaiting Analysis` for PENDING tests.
  - Green badge reading `Completed` or `Analyzed` for already-reported tests.

### 4.3 Patient Information section

A white card with a blue gradient header titled **Patient Information**. It shows four fields as slate-grey tiles:

- `Full Name`
- `Age` (shown as `42 years`)
- `Gender` — displayed as `Male` or `Female` (the backend sends `M` / `F`).
- `National ID`

Fields with no data show an italic `Not provided`.

### 4.4 Test Details & Timeline section

A white card with a green gradient header titled **Test Details & Timeline**. Up to three tiles:

- `Body Part` — the anatomical region examined.
- `Performed Date` — when the radiographer captured the images, formatted as e.g. `Oct 14, 2024`.
- `Reported Date` — when a report was submitted. This tile is only visible after a report exists.

### 4.5 Previous Analysis section (only if a report already exists)

If the test already has a submitted report, a green bar appears titled **Previous Analysis** containing up to four small white tiles:

- `Extent` — extent of disease.
- `Nodule` — nodule type.
- `Infiltrate` — infiltrate type.
- `Cavity` — cavity size.

Underscores in the stored values are replaced with spaces for readability.

### 4.6 Analysis Required notice

If the test is still `PENDING`, a light blue information strip appears just above the form reading:

> **Analysis Required:** Review the medical images above and complete the form below.

This is your cue to start reporting.

> **Note on ordering doctor context:** At the time of writing, the radiologist details page does not display a separate "clinical notes", "provisional diagnosis", or "investigation required" panel from the ordering doctor. The information available to you is the patient bio, the body part, the performed/reported dates, and the uploaded images. If you need the clinical context, contact the ordering doctor directly.

---

## 5. Scenario: Viewing Uploaded Medical Images

**Goal:** Open and examine the radiographer's uploaded images.

### 5.1 Finding the images on the details page

1. Open the test (Section 4).
2. Scroll to the section titled **Medical Images (N)** where `N` is the number of files attached.
3. Each image appears as a small tile in a responsive grid (2 columns on phones, 3 on tablets, 4 on desktops).

Each tile shows:

- A thumbnail icon with the label `Image 1`, `Image 2`, etc.
- The upload date below the label.
- A dark blue **View** button at the bottom of the tile.

If there are no images, a dashed grey placeholder appears reading `No images uploaded yet`.

### 5.2 Opening an image

1. Click the **View** button on the image tile you want to examine.
2. The app navigates to `/radiologist/view-image/:imageId` and the image viewer loads.

### 5.3 Navigating between multiple images

The image viewer opens one image at a time. To move between images on the same test:

1. Click the browser Back button to return to the test details page.
2. Click **View** on the next tile.

Open each image in turn. There is no built-in multi-image carousel on the radiologist viewer — each image is fetched via its ID.

### 5.4 DICOM and PNG rendering

The image data is fetched from the backend `/image/{image_id}/png` endpoint, which returns a rendered PNG stream. This means:

- DICOM files are server-rendered into PNG before they reach your browser. You see them as ordinary images.
- Very large files may take a few seconds to appear — the viewer shows a loader while it fetches.
- If the image fails to load, the viewer shows an error state. Go back and try again; if it persists, report the image ID to your administrator.

### 5.5 Viewer controls

The viewer provides the following controls (same as radiographer's viewer):

- **Zoom In / Zoom Out** — magnify or shrink.
- **Fullscreen** — toggle fullscreen reading.
- **Rotate** — rotate the image.
- **Brightness Up / Down**
- **Contrast**
- **Invert** — useful for X-ray positive/negative comparison.
- **Ruler / Measure** — click two points to measure distance.
- **Grid** — toggle a reference grid overlay.
- **Text annotation** — add text labels on findings.
- **Pan / Drag** — click and drag to move around when zoomed in.

When you are done examining, click the browser Back button to return to the test details page.

---

## 6. Scenario: Submitting a Radiology Report

**Goal:** Fill in and submit your report for a pending test.

### 6.1 Opening the form

1. Open the pending test (Section 4).
2. Scroll past the Medical Images section.
3. The form titled **Submit Radiology Analysis** appears at the bottom of the page.

If the test has already been reported, the form title instead reads **Edit Radiology Report** and fields are pre-filled — see Section 7.

### 6.2 Walking through every field

All radio-button fields below are **required**. If you try to submit without choosing one, a red error message appears under that group (e.g. `Please select extent of disease.`).

#### `extent_of_disease` — Extent of Disease

Pick exactly one radio button:

- `normal`
- `minimal disease`
- `moderately advanced disease`
- `far advanced disease`

#### `nodule_type` — Nodule Type

Pick exactly one:

- `miliary less than 3mm`
- `micronodules 3 to 6mm`
- `macronodules 6mm to 3cm`

#### `infiltrate_type` — Infiltrate Type

Pick exactly one:

- `alveolar`
- `interstitial`
- `mixed`

#### `cavity_size` — Cavity Size

Pick exactly one:

- `moderately advanced less than 4cm`
- `far advanced more or equal 4cm`

#### Clinical Findings checkboxes

Below the radio sections is a group headed **Clinical Findings** with five independent checkboxes. Tick the box only if the finding is present; leave unchecked if absent. They are not required — unchecked is interpreted as "absent / no".

- `pleural_effusion`
- `pleural_thickening`
- `mass_present`
- `hilar_adenopathy`
- `mediastinal_adenopathy`

#### `other_abnormalities` — Other Abnormalities (optional)

A free-text textarea labeled **Other Abnormalities (optional)** with placeholder text `any other abnormalities`. Use this to describe anything that does not fit the structured fields above. Leave it blank if there is nothing to add.

### 6.3 Submitting

1. Review every selection.
2. Click the blue **Submit Report** button at the bottom of the form. Its icon is a paper plane.
3. While the request is in flight, the button label changes to `Submitting...` and shows a spinning icon. The button is disabled during this time — do not click twice.
4. On success, a green toast appears in the top-right reading **`Report submitted successfully`**. The page then reloads so you see the updated state.
5. After the reload, the status badge at the top switches to green (`Completed`), the **Previous Analysis** section now shows your values, and the form re-titles itself to **Edit Radiology Report**.

### 6.4 What success means downstream

- The test moves out of your **Pending Reports** dashboard card.
- It shows up in your **Recent Reports** dashboard card.
- The ordering doctor can now see your findings on their patient view.

### 6.5 If the submit fails

- A red toast appears reading **`Failed to submit report`** or **`An error occurred while submitting the report`**.
- For validation problems, the toast title reads **`Please check your input`** and the description is a plain-English explanation (see Section 9).
- Your form entries are preserved. Fix the problem and click **Submit Report** again.
- If you lose internet connection, the toast reads **`Network Error`**. Reconnect and retry.

---

## 7. Scenario: Editing a Previously Submitted Report

**Goal:** Change values in a report you already submitted.

### 7.1 Finding an analyzed test

Option A — from the dashboard:

1. Sidebar → **Dashboard**.
2. Scroll to the **Recent Reports** card.
3. Click **View** on the report you want.

Option B — from the full list:

1. Sidebar → **Imaging Tests**.
2. In the search box, type the patient's name.
3. On the matching row, click **View**.

### 7.2 What's editable

On the test details page:

1. The header badge is green and reads `Completed` or `Analyzed`.
2. The **Previous Analysis** green strip shows the current values.
3. The form at the bottom is re-titled **Edit Radiology Report** with the sub-text: `Review and update the analysis below. Click "Update Report" to save changes.`
4. Every field from Section 6 is pre-filled with the saved values. You can change any of them:
   - All four radio groups (extent, nodule type, infiltrate type, cavity size).
   - All five clinical-finding checkboxes.
   - The `other_abnormalities` textarea.
5. To the right of the submit button, a small italic note shows `Last updated: <timestamp>`.

### 7.3 Saving your edits

1. Click the green **Update Report** button (icon: disk save).
2. While saving, the label becomes `Saving Changes...` with a spinner.
3. On success, a green toast appears reading **`Report updated successfully`** and the page reloads with the new values shown in the Previous Analysis strip.
4. On failure, a red toast reads **`Failed to update report`** or **`An error occurred while updating the report`**. Your edits stay on screen so you can retry.

What you cannot edit from this screen:

- The patient record itself.
- The uploaded images.
- The `performed_at` date (set by the radiographer).
- The `imaging_test_id` that links the report to its test.

If any of those are wrong, contact the radiographer or administrator.

---

## 8. Scenario: Viewing a Patient's Imaging History

**Goal:** See all past imaging studies for one patient.

The radiologist workspace does not have a dedicated "patient history" screen. You build the view yourself from the Imaging Tests list:

1. Sidebar → **Imaging Tests**.
2. In the **Search test type or status...** box, type the patient's name.
3. The table filters to show every row belonging to that patient — both PENDING items and your COMPLETED reports.
4. The **Time** column tells you the order (most recent first for reports, performed date for pending tests).
5. Click **View** on any row to open that specific study.
6. On the details page, the **Previous Analysis** strip (if present) shows what was found on that study.
7. Use the browser Back button between studies to return to the filtered list.

Tips:

- Searching only matches patient name text, so a partial name like `musoke` works.
- Rows with `Finding: Pending` are still awaiting analysis. Rows with a real finding value are reports you already filed.
- If you need the full patient chart (drugs, visits, other test types), ask a doctor — that view is not available in the radiologist role.

---

## 9. Common Error Messages — Plain English Meaning

When something goes wrong, the app shows a toast in the top-right corner. The titles and descriptions below come from `src/utils/networkUtils.ts`. Here is what each one actually means and what to do.

### 9.1 Network / connection errors

| Toast title | Toast description | What it means | What to do |
|---|---|---|---|
| **Network Error** | `Please check your internet connection and try again.` | Your browser is offline or cannot reach the server. | Reconnect to Wi-Fi / Ethernet, then retry. |

### 9.2 Validation errors (HTTP 422)

The toast title is **`Please check your input`** and the description is a humanized version of the backend message. The common ones for radiologists:

| You see | Plain meaning |
|---|---|
| `This field is required.` | A required radio group (extent, nodule, infiltrate, or cavity) was left unchosen. Select an option. |
| `A required selection is missing. Please pick an option from the list.` | A UUID-backed selection is empty. Usually means the imaging test ID did not load — reload the page. |
| `Please choose Yes or No for this field.` | A checkbox value arrived as text instead of a boolean. Reload and retry; if it persists, report to support. |
| `Please enter a valid number.` | A numeric field received an unparseable value. |
| `The patient record could not be found.` | The linked patient was deleted or moved. Contact the administrator. |
| `The selected visit could not be found.` | The visit linked to this test no longer exists. |
| `We couldn't find your doctor profile. Please contact your administrator.` | Your user account is not wired to a staff profile. |
| `Your account isn't fully set up yet. Please contact your administrator.` | Same idea — account incomplete. |
| `We couldn't load your facility information. Please try again.` | Transient facility lookup failure. Retry, then escalate. |

### 9.3 Permissions and authentication

| Toast title | Description | Meaning | What to do |
|---|---|---|---|
| **Access Denied** | `You don't have permission to perform this action.` | Your radiologist role cannot do that operation. | Do not retry. Contact the administrator. |
| (silent 401) | — | Your session expired. The app does not show a toast for this. | Refresh the page. You will be pushed to the login screen. Log in again. |

### 9.4 Server problems

| Toast title | Description | Meaning | What to do |
|---|---|---|---|
| **Not Found** | `The requested information could not be found.` (or humanized detail) | The test, image, or report ID does not exist on the server. | Return to the list and reopen the row. |
| **Something went wrong** | `We're having trouble right now. Please try again in a moment.` | Internal server error (500). | Wait a minute and retry. If it keeps happening, escalate with the test ID. |
| **Service Unavailable** | `The service is temporarily unavailable. Please try again later.` | The backend is down or restarting. | Wait and retry. |

### 9.5 Form-specific success and failure toasts

| Toast | When | Meaning |
|---|---|---|
| `Report submitted successfully` | After clicking **Submit Report** | New report saved. Page reloads. |
| `Report updated successfully` | After clicking **Update Report** | Edits saved. Page reloads. |
| `Failed to submit report` | Non-2xx response on submit | Report was not saved. Fix any validation toast and retry. |
| `Failed to update report` | Non-2xx response on edit | Edits were not saved. |
| `An error occurred while submitting the report` | Unexpected exception | Unknown client-side error. Reload and retry. |
| `An error occurred while updating the report` | Unexpected exception during edit | Same as above. |
| `Missing imaging test id. Please reload the page and try again.` | The form could not resolve the test ID | Hit browser refresh. |

---

## 10. Tips & Gotchas

### 10.1 Timezones

- Performed dates and reported dates are rendered using your device's local timezone (via `toLocaleDateString` / `toLocaleString`).
- Relative times like `2 hours ago` are also computed against your device clock. If your laptop clock is wrong, the relative times will look wrong.

### 10.2 Loading states

- **Shimmer placeholders** (grey animated rectangles) appear on the dashboard while stats load. They are normal.
- **Table skeleton rows** appear in the Pending Reports and Recent Reports cards while those lists load.
- A full-page spinner reading `Loading Imaging Tests` shows on the list page while the combined reports load.
- On the details page you may briefly see `Loading test details` before the content paints.

Never click Submit more than once. If the button is spinning, the request is in flight.

### 10.3 Mobile cards vs desktop tables

- On screens narrower than `md` (tablet/phone), tables collapse into stacked cards. The same four fields are shown with bold labels.
- All actions (**View**, **Submit Report**) are still available — they just appear as smaller pill buttons at the bottom of each card.

### 10.4 Empty-state screens

If a list has nothing in it, you will see a friendly placeholder instead of an empty table:

- Dashboard Pending Reports: title `No pending reports`, subtitle `Tests awaiting reports will appear here`.
- Dashboard Recent Reports: title `No reports found`, subtitle `Created reports will appear here`.
- Medical Images on a details page: `No images uploaded yet`.
- Test Not Found (invalid ID in the URL): red box with `Test Not Found` and the offending ID echoed back.

An empty state is not an error — it just means there is nothing to show yet.

### 10.5 Refreshing data

The app auto-refreshes reports and pending lists right after you submit or update a report. If you think the screen is showing stale data (for example, a new test the radiographer just uploaded is not appearing), navigate away to Dashboard and back to **Imaging Tests** to force a re-fetch.

### 10.6 Keeping your dashboard count accurate

- The **Pending** metric reflects how many tests are still awaiting analysis at your facility scope.
- The **Reports Today** metric resets at midnight server-time, not at your local midnight — so late-night entries may fall into a different "day" than you expect.
- The **Total Reports Created** metric includes edits to old reports? No — editing does not increment the counter; only fresh submissions do.

### 10.7 Do not close the tab mid-submit

If you close the browser while `Submitting...` is showing, the request may or may not reach the server. Always wait for the success toast and the page reload before navigating away.

---

*For general navigation, login, and settings details shared across roles, see the [General System Guide](./00-general-system-guide.md).*
