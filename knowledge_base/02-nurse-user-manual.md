# Nurse User Manual

This manual is written as a recipe book. Each scenario is a numbered, click-by-click walkthrough that tells you exactly what to click, what to type, and what you will see on screen. If something goes wrong, look up the toast message in section 8.

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Dashboard Tour](#2-dashboard-tour)
3. [Scenario: Registering a new patient](#3-scenario-registering-a-new-patient)
4. [Scenario: Adding medical history for a patient](#4-scenario-adding-medical-history-for-a-patient)
5. [Scenario: Assigning a doctor to a patient](#5-scenario-assigning-a-doctor-to-a-patient)
6. [Scenario: Viewing my added patients vs. facility patients](#6-scenario-viewing-my-added-patients-vs-facility-patients)
7. [Scenario: Updating a patient's bio or medical history later](#7-scenario-updating-a-patients-bio-or-medical-history-later)
8. [Common error messages — plain English meaning](#8-common-error-messages--plain-english-meaning)
9. [Tips and gotchas](#9-tips-and-gotchas)

---

## 1. Getting Started

### Logging in

1. Open your browser and go to the DSI MDR-TB web app URL provided by your facility administrator.
2. On the login screen, type your work email in the `Email` field.
3. Type your password in the `Password` field.
4. Click the **Sign In** button.
5. If your credentials are correct, you will land on the **Nurse Dashboard** at `/nurse`.

### Where you land

After login, the page header reads **"Welcome back, [Your First Name]!"** and you see four metric cards followed by a "Recently Added Patients" table.

### Logging out

1. Open the sidebar (it is visible on desktop; on mobile click the menu icon in the top bar).
2. Click **Log Out** at the bottom of the sidebar.
3. You will be returned to the login screen and your session will end.

### Resetting your password

1. On the login screen, click **Forgot password?**.
2. Enter your work email and click **Send reset link**.
3. Check your inbox for an email from the system. Click the link inside.
4. Enter a new password twice and click **Reset Password**.
5. Log in again with the new password.

If you do not receive the email within a few minutes, check your spam folder, then ask your facility administrator to verify the email on file.

---

## 2. Dashboard Tour

**URL:** `/nurse`

The dashboard has four parts: a welcome banner, four metric cards, a "Recently Added Patients" table, and the sidebar.

### Welcome banner

A blue gradient banner at the top reads **"Welcome back, [Your First Name]!"** followed by *"Here's an overview of your patient management activities"*. This is purely informational.

### The four metric cards

| Card | What the number means |
|------|----------------------|
| **Total Patients** | Every patient currently linked to your account. |
| **Assigned to Doctor** | Patients from your list who already have a doctor attached. |
| **Needs Assignment** | Patients you have registered who do **not** yet have a doctor. These are the ones you should action next. |
| **Incomplete History** | Patients missing the medical history form. Open these and click **Update History**. |

The numbers update automatically when you register a patient, add medical history, or assign a doctor.

### Recently Added Patients table

This table shows the **5 most recently registered patients** linked to you, sorted by registration date (newest first).

Columns from left to right:

| Column | Shows |
|--------|-------|
| `Patient Name` | First and last name. On mobile this row also shows the phone number. |
| `Contact` | Email and phone (hidden on small screens). |
| `Doctor` | Either the assigned doctor name or an amber "Unassigned" badge. |
| `Registered` | The date you (or another nurse) created the record. |
| `Medical History` | A blue **Update History** button. |
| `Assign Doctor` | Either an **Assign Doctor** button or a green **Assigned** badge. |
| `View Details` | A **View** button that opens the full patient profile. |

If the table shows a shimmer/skeleton, the data is still loading. Wait a few seconds.

If the table is completely empty, you will see a "No patients yet" message and a single **Add Patient** button. Click it to register your first patient.

To see the full list, click **View All** above the table — this takes you to **Facility Patients**.

---

## 3. Scenario: Registering a new patient

This is the most common task. Follow it from start to finish.

**You start on:** the Dashboard (`/nurse`).
**You will end on:** the Add Medical History page for the new patient.

### Step 1 — Open the registration form

1. From the Dashboard, look at the top-right of the page.
2. Click the **Add Patient** button (white button with a `+` icon, or in the sidebar use **My Added Patients > Add Patient**).
3. The page changes to **Patient Registration**. You will see a blue header reading *"Patient Registration — Enter patient biographical information to begin the registration process"*.
4. Below the header, a progress strip shows two steps: **1. Patient Info** (highlighted) and **2. Medical History** (greyed out). You are on step 1.

### Step 2 — Fill the Personal Information section

This is the first white card with a person icon.

1. `First Name` — type the patient's legal first name (example: `Mary`). Required.
2. `Last Name` — type the patient's legal last name (example: `Nakato`). Required.
3. `Phone Number` — choose the country code from the small dropdown (defaults to Uganda `+256`), then type the rest of the digits. The field accepts Ugandan, Kenyan, Rwandan and Tanzanian numbers. Required.
4. `Email` — optional. Type the patient's email if they have one.
5. `Age` — optional. Type a whole number (example: `34`).
6. `Gender` — click the dropdown and pick **Male** or **Female**. Required.
7. `National ID` — optional. Type the National ID number exactly as printed on the card (example: `CM12345678ABCD`).

### Step 3 — Fill the Address Information section

The next card has a pin icon. The address fields cascade — picking a region filters the districts, picking a district filters the counties, and so on. **Always work top-down.**

1. `Country` — pre-filled with **Uganda**. Leave it as is.
2. `Region` — click and pick the region.
3. `District` — click and pick a district. The list only contains districts inside the chosen region.
4. `County` — pick a county inside that district.
5. `Sub County` — pick a sub-county inside that county.
6. `Parish` — pick a parish.
7. `Village` — pick a village.
8. `Nearest Health Unit` — type the name of the closest health centre (free text).

If a dropdown is empty when you click it, the parent field above it has not been picked yet. Go up and pick it first.

### Step 4 — Fill the Next of Kin section

This card has a group-of-people icon and is split into two parts.

**Part A — Contact Information:**

1. `Full Name` — type the next of kin's full name.
2. `Contact Person type` — pick one of: **Parent**, **Spouse**, **Sibling**, **Child**, **Relative**, **Friend**, **Other**. This is the legal/category type.
3. `Relationship` — this is a separate dropdown listing the actual relationship. Pick one of:
   - **Father**
   - **Mother**
   - **Brother**
   - **Sister**
   - **Spouse**
   - **Guardian**
   - **Friend**
   - **Other**
4. `Phone Number` — same format as the patient phone (country code + digits).
5. `Email (Optional)` — leave blank if they have none.
6. `ID Type` — pick **National ID**, **Passport**, **Driving License**, **Voter Card**, or **Other**.
7. `ID Number` — type the number from the chosen ID document.

**Part B — Next of Kin's Address:**

Repeat the same cascading address fields you filled for the patient (Region → District → County → Sub County → Parish → Village). If they live at the same address as the patient, you still have to pick each level manually.

### Step 5 — Fill the Socio-economic Information section

This card has a house icon.

1. `Education Level` — pick **None**, **Primary Education**, **Secondary Education**, or **Tertiary Education**.
2. `Number of Rooms` — type the number of rooms in the house (minimum `1`). Used to compute household density.
3. `Number of People` — type how many people live in the house (minimum `1`).
4. `House Ownership` — pick **Rented**, **Personal**, or **Employer Owned**.

The system auto-calculates household density (people ÷ rooms) and stores it for you. You do not type it.

### Step 6 — Save the patient

1. Scroll to the bottom right.
2. Click the dark blue **Save and Continue** button (with a right-arrow icon).
3. The button changes to a spinner reading **"Registering..."**. Do not click it again.

### Step 7 — What happens next

On **success**:

- You see a green toast: **"Patient created (ID: ...)"**.
- The page automatically navigates to **Add Medical History** for that new patient (`/nurse/add-medical-history/[patientId]`).
- You can now follow the next scenario (section 4).

On **failure**, you stay on the form. The most common errors are:

| Toast title | What it really means | What to do |
|-------------|---------------------|------------|
| `Please check your input` | One or more required fields are missing or wrong. | Scroll up. The faulty field will be highlighted in red with a message under it. Fix and click **Save and Continue** again. |
| `Patient already exists` | A patient with the same email, phone, or National ID is already in the system. | The matching field (`Email`, `Phone Number`, or `National ID`) will turn red. Either change it or open the existing patient instead of creating a duplicate. |
| `Network Error` | Your computer lost internet. | Reconnect to Wi-Fi/data and click **Save and Continue** again. Your typed data is **not** lost. |
| `Validation error` | A specific field failed a server check. The toast description shows which field. | Read the description, fix the field, and resubmit. |

If you see something else, look it up in section 8.

---

## 4. Scenario: Adding medical history for a patient

**You start on:** the Add Medical History page (`/nurse/add-medical-history/[patientId]`). You land here automatically after registering a patient, or by clicking **Update History** next to any patient.

The page header shows the patient's full name with a Male/Female badge. The title reads **"Add Patient Medical History"** the first time and **"Update Patient Medical History"** the second time onwards. The progress strip shows step 1 ticked green and step 2 active.

### Step 1 — Patient Type

Card with a person icon at the top.

1. Under `Select Patient Type`, click one of the three radio buttons:
   - **New** — never been treated for TB.
   - **Previously Treated** — has been on TB treatment before.
   - **Treatment History Unknown** — you cannot confirm.
2. Just below, the checkbox `Previously diagnosed with TB` controls whether the patient has ever had a confirmed TB diagnosis. Tick it only if they say **Yes**.

### Step 2 — Risk Group Assessment

Card with a shield icon. You see a 3-column grid of checkboxes.

1. Tick every applicable risk factor:
   - **Allergies**, **Consumes Alcohol**, **Chronic Cough**, **Diabetic**, **Fisher Folk**, **Healthcare Worker**, **On Medication**, **Mentally Ill**, **Miner**, **Pregnant**, **Prisoner**, **Refugee**, **TB Contact**, **Tobacco User**, **Uniformed Personnel**.
2. If a relevant factor is not in the list, type it into the `Other Risk Factors` text box at the bottom.
3. None of these are individually required, but be honest — they drive risk scoring.

### Step 3 — Symptoms Assessment

Card with a heart icon.

1. Tick every symptom the patient is currently experiencing from the 3-column grid:
   - **Chest pain**, **Chills**, **Cough**, **Coughing blood/sputum**, **Dyspnea**, **Fever**, **Night sweats**, **No appetite**, **Weakness/Fatigue**, **Weight loss**.
2. **Validation rule:** you must tick **at least one symptom** OR type something in `Other Symptoms` below. If you tick none and leave the box empty, the form will refuse to save with the message *"At least one symptom is required or describe other symptoms"*.
3. `Temperature (°C)` — required. Type the body temperature in Celsius (example: `37.5`). Must be between **30** and **50**. Decimals are allowed.
4. `Other Symptoms` — optional free text for anything not in the checkbox list.

### Step 4 — Physical Measurements

Card with a scale icon.

1. `Weight (kg)` — required. Type the weight in kilograms (example: `64.5`). Must be greater than **0** and less than **500**. Decimals are allowed.
2. `Height (cm)` — required. Type the height in centimetres (example: `168`). Must be between **30** and **300**.

### Step 5 — Health Status

Card with a beaker icon.

1. `HIV Status` — required. Pick **Negative** or **Positive**. If unknown, ask the patient to take a test before continuing.

### Step 6 — Submit

1. Scroll to the bottom.
2. Click the gradient blue **Submit Medical History** button.
3. The button shows a spinner reading **"Submitting..."**.

### What happens next

On **success**:

- You see a green toast: **"Medical history added successfully"** (or *"Medical history updated successfully"* if the record existed before).
- You are sent back to the Nurse Dashboard. The patient's "Incomplete History" indicator disappears.

On **failure**:

- You see a red toast: **"Failed to add medical history"** (or *"Failed to update medical history"*) with a description of the problem.
- The form stays as it is. Read the toast, fix the highlighted field, and click **Submit Medical History** again.

Common reasons for failure:

| Cause | Fix |
|-------|-----|
| You left `Temperature`, `Weight`, `Height`, or `HIV Status` empty. | Scroll up, fill in the red-bordered field, resubmit. |
| You did not tick any symptom and did not write in `Other Symptoms`. | Tick at least one symptom checkbox or describe one in the textbox. |
| You did not pick a `Patient Type` radio button. | Pick **New**, **Previously Treated**, or **Treatment History Unknown**. |
| Network dropped. | Reconnect and click submit again. |

---

## 5. Scenario: Assigning a doctor to a patient

**You start on:** any page that lists patients — the Dashboard, **Facility Patients**, or **My Added Patients**.

### Step 1 — Find the patient row

1. Scroll the table until you see the patient.
2. Look at the **Assign Doctor** column.
   - If the column shows a green **Assigned** badge, the patient already has a doctor — there is nothing to do.
   - If the column shows a green-bordered **Assign Doctor** button, continue.

### Step 2 — Open the assignment dialog

1. Click the **Assign Doctor** button on that row.
2. A small dialog opens titled **"Assign Patient to a Doctor"**, with the description *"Select a doctor to assign this patient."*.

### Step 3 — Pick a doctor

1. Inside the dialog, click the dropdown labelled *"select a doctor"*.
2. The dropdown lists every doctor in your facility by full name.
3. If the dropdown shows a spinner with the text **"Loading doctor list"**, wait a few seconds for it to populate.
4. Click the doctor you want to assign.

### Step 4 — Confirm

1. Click the dark **Assign Doctor** button at the bottom-right of the dialog.
2. The button shows a spinner reading **"Assigning..."**.
3. On success the dialog closes by itself, you see a green toast **"Doctor assigned successfully"**, and the row updates so the button becomes a green **Assigned** badge.

### If something goes wrong

| Toast | Meaning | Fix |
|-------|---------|-----|
| **"Failed to assign doctor"** | The server rejected the assignment. The description tells you why. | Read the description. If it says the doctor is not available or the patient is missing, refresh the page and try again. |
| Dropdown is empty | No doctors are registered at your facility yet. | Tell your facility administrator. You cannot assign until at least one doctor exists. |
| `Network Error` | You lost internet. | Reconnect, reopen the dialog, retry. |

To cancel without assigning, click **Cancel** in the dialog footer or click outside the dialog.

---

## 6. Scenario: Viewing my added patients vs. facility patients

There are two patient lists. They look similar but contain different rows.

### The difference

| List | URL | What it contains |
|------|-----|------------------|
| **My Added Patients** | `/nurse/my-added-patients` | Only the patients **you personally registered** with your account. |
| **Facility Patients** | `/nurse/facility-patients` | **Every** patient registered at your facility, regardless of who created them (other nurses, doctors, you). |

If you only want to see your own work, use My Added Patients. If you need to find a patient another nurse registered, use Facility Patients.

### How to switch between them

1. Open the sidebar.
2. Click **My Added Patients** (nurse icon) — this opens your personal list.
3. Click **Facility Patients** (hospital-user icon) — this opens the facility-wide list.

### How to filter

Both pages have a filter dropdown at the top of the table.

1. Click the **Filter** dropdown.
2. Pick one of:
   - **All Patients** — default, shows everything.
   - **No Medical History** — only patients whose medical history form is missing. Use this to clean up incomplete records.
   - **Unassigned to Doctor** — only patients with no doctor attached. Use this with section 5 above.
3. The table updates immediately. The three statistic cards at the top of Facility Patients (`Total Patients`, `Unassigned`, `Incomplete History`) always show **the unfiltered** counts so you know how big the backlog is.

### How to find a specific patient

1. The tables support sorting — click any column header marked sortable (`Patient Name`, `Registration Date`) to sort A→Z or by date.
2. To open a single patient, click the **View** button at the far right of the row. This takes you to `/nurse/patient/[patientId]`.

### Empty state

If no patients match your filter, the table is replaced with a message:

- **"No patients found"** with an **Add Patient** button — appears when you have no patients at all, or when a filter has no matches.
- Just clear the filter back to **All Patients** if you expected to see rows.

---

## 7. Scenario: Updating a patient's bio or medical history later

You cannot edit a patient's biographical record (name, address, next of kin, etc.) from the nurse interface — it is locked once saved. If something is wrong with the bio, contact your facility administrator.

You **can** update medical history at any time. Here is how.

### Step 1 — Find the patient

1. Open **My Added Patients** or **Facility Patients**.
2. Find the row for the patient.

### Step 2 — Open the medical history form

1. Click the blue **Update History** button in the `Medical History` column. Alternatively click **View** on the row, then click **Add Medical History** in the patient details header.
2. You land on `/nurse/add-medical-history/[patientId]`. The page title now reads **"Update Patient Medical History"** and every field is pre-filled with the existing values.

### Step 3 — Edit and resubmit

1. Change any of the checkboxes, dropdowns, or numbers as needed.
2. Note: `Weight` and `Height` are not pre-filled (they are taken at every visit). Re-enter them.
3. Click **Submit Medical History**.
4. On success a green toast reads **"Medical history updated successfully"** and you return to the Dashboard.

### What is editable vs. locked

| Section | Editable by nurse? |
|---------|--------------------|
| Patient bio (name, phone, email, address, next of kin, education, housing) | Locked. Contact admin to change. |
| Patient type, risk group, symptoms, temperature, weight, height, HIV status, ever-diagnosed-with-TB | Editable through **Update History**. |
| Doctor assignment | Editable through **Assign Doctor**, but only while the patient has no doctor. To re-assign after the fact, ask an admin. |

---

## 8. Common error messages — plain English meaning

When the server rejects something, the system translates the technical message into plain English before showing it to you. Here is the lookup table. The left column is the toast you will see. The middle column is what is actually wrong. The right column is what to do.

| Toast you see | What it really means | What to do |
|---------------|---------------------|------------|
| **Please check your input** | One or more form fields failed validation. The toast description names the specific issue. | Scroll up; the bad field is outlined red. Fix it and resubmit. |
| **Please choose Yes or No for this field.** | A Yes/No field (like a checkbox or radio) was left in an in-between state. | Pick a clear Yes or No on the highlighted field. |
| **Please enter a valid number.** | You typed letters into a number field, or the field is blank. | Clear the field and type only digits (and a decimal point if needed). |
| **This field is required.** | A required field was left empty. | Fill it in. Required fields are marked with a red asterisk. |
| **A required selection is missing. Please pick an option from the list.** | A dropdown that needed a choice was left blank. | Click the dropdown and pick a value. |
| **Your account isn't fully set up yet. Please contact your administrator.** | The server cannot find your full nurse profile. | Stop work, contact your facility administrator. You will not be able to register or assign until they fix it. |
| **We couldn't load your facility information. Please try again.** | The server failed to fetch your facility info. | Refresh the page. If it keeps happening, contact admin. |
| **The patient record could not be found.** | The patient you tried to open has been deleted, or the link is wrong. | Go back to the patient list and pick the patient again. |
| **No patients are linked to your account yet.** | You have not registered anyone yet (or none are visible to you). | Click **Add Patient** to register your first patient. |
| **Network Error** | Your computer is offline or the server is unreachable. | Check your internet, then retry. Your form data is not lost. |
| **Access Denied** | You tried to do something nurses are not allowed to do. | Stop. Ask the relevant role (doctor or admin) to do it. |
| **Something went wrong** | The server hit an unexpected error. | Wait a minute and retry. If it keeps happening, contact admin. |
| **Service Unavailable** | The server is down for maintenance. | Wait a few minutes and try again. |
| **Session Expired** / silent logout | You have been logged out due to inactivity. | Log in again with your email and password. Any unsaved form data will be lost. |
| **Patient already exists** | Email, phone, or National ID matches an existing patient. | Search for the existing patient instead of creating a duplicate. |
| **Failed to assign doctor** | The doctor assignment did not save. | Read the description, refresh, retry. |
| **Failed to add medical history** / **Failed to update medical history** | The medical history form did not save. | Check the description for the field at fault, fix, resubmit. |

---

## 9. Tips and gotchas

- **Times are local.** Visit times and registration dates are shown in your computer's local timezone, not UTC. Two devices in different countries will see slightly different timestamps.
- **Shimmer placeholders mean loading.** If you see grey blocks pulsing where text should be, the data is still loading from the server. Wait a few seconds — do not click anything.
- **Tables become cards on mobile.** On a phone, the patient tables collapse into vertical cards showing just the most important fields (name, phone, View button). Use a tablet or laptop if you need full visibility.
- **Empty lists guide you.** If a list is empty, the empty-state panel always tells you the next sensible action — usually an **Add Patient** button.
- **Cascading address dropdowns must be filled top-down.** If District is empty when you click it, go back and pick a Region first.
- **Save and Continue does both jobs.** Clicking it on the registration form not only saves the patient but also opens the medical history page for that patient — you do not need to navigate manually.
- **Re-typing weight and height.** Even when updating an existing medical history, you must re-enter weight and height. They are treated as fresh measurements.
- **Do not double-click submit buttons.** When the button shows "Registering...", "Submitting...", or "Assigning...", the request is in flight. Clicking again will not speed it up and may cause duplicate records.
- **The four dashboard cards reflect your patients only.** "Total Patients" on the dashboard is your linked patients, not the whole facility. To see facility-wide totals, open **Facility Patients**.
- **Settings.** For password change, profile, and notification preferences see the [General System Guide — Settings](./00-general-system-guide.md#6-settings).

---

*For general navigation, login, and shared settings, see the [General System Guide](./00-general-system-guide.md).*
