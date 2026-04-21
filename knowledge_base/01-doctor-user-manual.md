# Doctor User Manual

This manual is written as a set of recipes. Each scenario is a numbered, click-by-click walkthrough that tells you exactly what to click, what to type, and what to do if something goes wrong. You can jump straight to any section without reading the earlier ones.

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Dashboard Tour](#2-dashboard-tour)
3. [Scenario: Registering a brand new patient](#3-scenario-registering-a-brand-new-patient)
4. [Scenario: Finding a returning patient assigned to you](#4-scenario-finding-a-returning-patient-assigned-to-you)
5. [Scenario: Starting a new visit for a patient](#5-scenario-starting-a-new-visit-for-a-patient)
6. [Scenario: Ordering a Lab Test](#6-scenario-ordering-a-lab-test-gene-xpert--sputum-conversion--other)
7. [Scenario: Ordering an Imaging Test](#7-scenario-ordering-an-imaging-test-chest-x-ray--ct-scan)
8. [Scenario: Adding Medical History](#8-scenario-adding-medical-history-enhanced-medical-history-form)
9. [Scenario: Prescribing medication](#9-scenario-prescribing-medication)
10. [Scenario: Reviewing test results](#10-scenario-reviewing-test-results)
11. [Scenario: Using AI Insights / MDR-TB prediction](#11-scenario-using-ai-insights--mdr-tb-prediction)
12. [Common error messages — plain English meaning](#12-common-error-messages--plain-english-meaning)
13. [Tips & gotchas](#13-tips--gotchas)

---

## 1. Getting Started

### Logging in

1. Open your web browser (Chrome, Edge, or Firefox) and go to the address your facility administrator gave you for the DSI MDR-TB system.
2. You will see a login page asking for your **Email** and **Password**.
3. Type your work email in the `Email` field.
4. Type your password in the `Password` field.
5. Click the **Sign In** button.
6. If your credentials are correct, the page will navigate to your **Doctor Dashboard** at the URL `/doctor`.
7. If your credentials are wrong, an error toast appears at the top-right of the screen. The most common ones are:
   - **"Unauthorized - Please login again"** — your email or password is wrong. Try again.
   - **"Network Error"** — your internet is down. Check your connection.
   - **"Your account isn't fully set up yet."** — your account exists but is not yet linked to a doctor profile. Contact your facility administrator.

### Where you land after login

After a successful login you will see the **Doctor Dashboard**. The left side of the screen has a sidebar menu, and the main area shows your metrics, recent test orders, and assigned patients. See [Section 2: Dashboard Tour](#2-dashboard-tour).

### How to log out

1. Look at the sidebar on the left.
2. Click **Log Out** at the bottom of the menu.
3. You will be returned to the login page. Your session is now ended.

### How to reset your password if you forget it

The system does not currently provide a self-service password reset for doctors. If you forget your password:

1. Contact your facility administrator.
2. Ask them to reset your password from their administrator account.
3. They will give you a new temporary password. Log in with it and then change it from the **Settings** page.

---

## 2. Dashboard Tour

**URL:** `/doctor`

The dashboard is the page you see right after logging in. It is divided into the following parts.

### The three metric cards (top of the page)

These are colored cards showing your workload at a glance.

1. **Total Visits** (yellow) — the total number of patient visits you have ever conducted.
2. **In Progress** (red) — the number of patients currently assigned to you.
3. **New Patients** (green) — the number of patients you personally registered.

These cards are read-only. They are just for information.

### Your name and facility

Below the metric cards, the system shows:

- **Dr. [Your First Name] [Your Last Name]**
- The facility you are assigned to.

If you see **"We couldn't load your facility information."** here, the backend cannot find your facility. Try refreshing the page; if it persists, contact your administrator.

### Imaging Tests card

- Shows the **4 most recent** imaging test orders you created.
- Columns: `Test Type`, `Status`, `Patient Name`, `Ordered Date`.
- Click **View All Test Orders** at the bottom of the card to open the full Test Orders page.

### Lab Tests card

- Shows the **4 most recent** lab test orders you created.
- Columns: `Test Type`, `Status`, `Patient Name`, `Ordered Date`.
- Click **View All Test Orders** at the bottom of the card to open the full Test Orders page.

### Assigned Patients card

- Shows the first **4** patients currently assigned to you.
- Columns: `Patient Name`, `Assigned Doctor`, `Age`, `Contact`, `Actions`.
- Click **View Details** in the Actions column to open a patient.
- Click **View All Patients** to open the full patient list.

### Sidebar menu

| Menu item | What it does |
|-----------|--------------|
| **Dashboard** | Returns to this page (`/doctor`). |
| **Manage Patients** | Opens the list of patients assigned to you (`/doctor/patients`). |
| **My Added Patients** | Opens the list of patients you personally registered (`/doctor/my-added-patients`). |
| **Test Orders** | Opens the full list of all lab and imaging tests you have ordered (`/doctor/test-orders`). |
| **Settings** | Opens your profile and password settings (`/doctor/settings`). |
| **Log Out** | Ends your session and returns to the login page. |

---

## 3. Scenario: Registering a brand new patient

Use this when a new patient walks into the clinic and is not yet in the system. By the end of this scenario the patient will be saved and you will be on the medical history page.

### Step 1: Open the registration form

1. From the sidebar, click **Manage Patients**. You are now at `/doctor/patients`.
2. In the blue header at the top right, click the **Register New Patient** button (it has a `+` icon).
3. You are now on the patient type selection page (`/doctor/patients/add-patient-type`).

### Step 2: Choose the patient type

1. Pick the patient type that matches the patient (for example, **TB Patient**).
2. Click **Continue**. You are now on the bio information form at `/doctor/patients/add-patient`.

### Step 3: Fill in Section A — Bio Information

1. **First Name** — type the patient's first name. Letters only, minimum 2 characters.
2. **Last Name** — type the patient's last name. Letters only, minimum 2 characters.
3. **Phone Number** — type the patient's phone number in Ugandan format. Acceptable forms: `0772123456` or `+256772123456`.
4. **Email** — optional. If you enter one, it must be a valid email address (must contain `@`).
5. **Age** — optional. Must be 0 or higher.
6. **Gender** — click the dropdown and pick **Male** or **Female**. This field is required because the medical history form uses gender to decide whether to show the "pregnant" question.
7. **National ID** — optional. The system expects the format `CM` or `CF` followed by 12 alphanumeric characters (for example, `CM1234567890AB`).

### Step 4: Fill in Section B — Address Information

All fields in this section are optional, but fill in as many as you can:

1. `Region`, `District`, `County`, `Sub County`, `Parish`, `Village`, `Country`, `Nearest Health Unit` — type the values that apply.

### Step 5: Fill in Section C — Next of Kin

All fields are optional but recommended:

1. `Full Name` — the relative's name.
2. `Contact Person Type` — pick one of: **Parent**, **Spouse**, **Sibling**, **Child**, **Relative**, **Friend**, **Other**.
3. `Relationship` — free text describing the relationship.
4. `Contact Phone` — phone number in the same format as the patient phone.
5. `Email` — optional, must be a valid email.
6. `Identification Type` — pick one of: **National ID**, **Passport**, **Driving License**, **Voter Card**, **Other**.
7. `Identification Number` — the ID number.
8. Then fill the next-of-kin address fields the same way you filled Section B.

### Step 6: Fill in Section D — Socio-economic Information

1. **Education Level** — pick one: **None**, **Primary Education**, **Secondary Education**, **Tertiary Education**.
2. **Household Density** — pick one: **Low**, **Medium**, **High**.
3. **House Ownership** — pick one: **Rented**, **Personal**, **Employer Owned**.

### Step 7: Save the patient

1. Click the **Save and Continue** button at the bottom of the form.
2. While the system is saving, the button shows a spinner and is disabled — do not click it again.
3. On success, a green toast appears confirming the patient was created and you are automatically taken to the **Enhanced Medical History** page for this new patient. See [Section 8](#8-scenario-adding-medical-history-enhanced-medical-history-form) for the next steps.

### What can go wrong

| Toast you may see | What it means | What to do |
|---|---|---|
| **"Please check your input"** | A required field is empty or invalid. | Scroll up; the offending fields will have red text under them. |
| **"This field is required."** | You missed a required field. | Fill it in and click **Save and Continue** again. |
| **"Your account isn't fully set up yet."** | The backend cannot find your doctor profile. | Contact your administrator — your user account is not linked to a doctor record. |
| **"We couldn't load your facility information."** | The backend cannot find your facility. | Try again. If it persists, contact your administrator. |
| **"Network Error"** | You are offline. | Check your internet and try again. |

---

## 4. Scenario: Finding a returning patient assigned to you

Use this when a patient you have seen before comes back, or when a new patient has been assigned to you by your administrator.

### Step 1: Open your patient list

1. From the sidebar, click **Manage Patients**. You are now at `/doctor/patients`.
2. The page shows a table of every patient currently assigned to you.

### Step 2: Find the patient

1. Look for the patient by name in the **Patient Name** column.
2. To sort the table, click any column header (`Patient Name`, `Age`).
3. If you registered the patient yourself rather than being assigned them, click **My Added Patients** in the sidebar instead.
4. If the list is empty, you will see an empty-state illustration with the message **"No patients are linked to your account yet."** This means your administrator has not assigned anyone to you yet.

### Step 3: Open the patient

1. In the patient's row, click the **View Details** button in the **Actions** column.
2. You are now on the patient details page (`/doctor/patients/patient/[id]`).

### Step 4: View their existing history

The patient details page has 5 tabs at the top. Click each tab to see different information.

1. **Overview** — demographics, address, next of kin, medical history, symptoms, risk factors.
2. **Visits** — every visit the patient has ever had.
3. **Tests** — every lab and imaging test ordered for the patient.
4. **AI Insights** — MDR-TB treatment response predictions.
5. **Prescriptions** — every medication prescribed.

To read the medical history, stay on the **Overview** tab. The information is grouped into expandable sections. Click any section header to open or close it.

---

## 5. Scenario: Starting a new visit for a patient

Every clinical action (lab tests, imaging tests, prescriptions) must be tied to an **active visit**. If a patient does not have an in-progress visit, you must start one first.

### Step 1: Open the patient

1. From the sidebar, click **Manage Patients**.
2. Find the patient and click **View Details**.

### Step 2: Open the Visits tab

1. Click the **Visits** tab at the top of the patient details page.
2. You will see a table listing every previous visit.

### Step 3: Open the new visit dialog

1. Click the **New Visit** button in the page header.
2. A dialog box appears titled **New Visit**.

### Step 4: Pick the visit type

Click the **Visit Type** dropdown and select one of:

| Visit type | When to use it |
|---|---|
| **Consultation** | A normal walk-in clinic consultation. |
| **Baseline Visit** | The very first visit when treatment is starting — used as the baseline for later comparisons. |
| **Two Month** | The follow-up visit at the 2-month mark of treatment. The AI prediction feature is most useful from this visit onward. |
| **Five Month** | The follow-up visit at the 5-month mark. |
| **Other** | Any visit that does not fit the above. |

### Step 5: Add the initial note

1. Click in the **Initial Note** text area.
2. Type a short clinical note describing why the patient is here today (for example: `Patient reports persistent cough and chest pain for 3 weeks`).
3. This field is required. If you leave it blank, you will see the red error **"Please select a visit type and enter an initial note."**

### Step 6: Save the visit

1. Click **Create Visit**.
2. While saving, the button shows **"Creating..."** and is disabled.
3. On success the dialog closes, and the new visit appears at the top of the visits table with the status badge **In Progress** in amber.

### Step 7: When you finish the visit

1. Find the in-progress visit row in the table.
2. Click the **End Visit** button in the **Actions** column.
3. The status badge changes from amber **In Progress** to green **Completed**.

### What about the time on the visit?

Visit start and end times are now displayed in **your local timezone**. Earlier versions had a 3-hour offset; that is fixed. If a visit shows a time three hours off, refresh the page.

### What if I see "no active visit" warnings?

If you try to order a test or write a prescription and there is no in-progress visit, the system blocks you and shows a warning. Come back here, click **New Visit**, and create one first.

---

## 6. Scenario: Ordering a Lab Test (Gene Xpert / Sputum Conversion / Other)

You can only order a lab test for a patient who has an **in-progress visit**. If they don't have one, follow [Section 5](#5-scenario-starting-a-new-visit-for-a-patient) first.

### Step 1: Open the patient and find the active visit

1. Sidebar > **Manage Patients** > click **View Details** on the patient.
2. Click the **Visits** tab.
3. Locate the row showing the amber **In Progress** badge.

### Step 2: Open the Order Test action

You have two ways:

- **From the Visits tab:** click the **Order Test** button in the row's Actions column, then choose **Lab Test** in the dialog.
- **From the Tests tab:** click the **Tests** tab, then click the **Order New Test** button in the top right. If the button is disabled, you have no active visit — go back to Step 1.

The **Create Lab Test Order** dialog opens, with the title **"Create Lab Test Order"** and the description **"Fill out the form to order a new lab test"**.

### Step 3: Confirm the IDs

The `Patient ID` and `Visit ID` fields are auto-filled and grayed out. You cannot change them. They tell the system which patient and visit this lab test belongs to.

### Step 4: Choose the test type

1. Click the **Test Type *** dropdown.
2. Pick one of:
   - **Gene Xpert**
   - **Sputum Conversion**
   - **Other**

### Step 5: If you picked "Other", specify the test name

When you pick **Other**, a new field appears immediately below the dropdown labeled **Specify Test Name *** with a placeholder `e.g. AFB Smear, Culture, etc.`.

1. Click in that field.
2. Type the exact name of the test you want, for example `AFB Smear` or `Culture`.
3. **You must fill this in.** If you leave it blank and click submit, you will see the red message **"Please enter the test name"** under the field, and a toast **"Please enter the test name for the 'Other' option"**. You may also see the toast **"Please check your input"** with the description **"Please enter the test name when selecting 'Other'."** if the validation fires from the backend.

### Step 6: Write the reason for examination

1. Click in the **Reason for Examination *** text area.
2. Type a clear clinical reason — at least **10 characters**. For example: `Suspected MDR-TB based on persistent cough and prior treatment failure`.
3. If you type fewer than 10 characters, you'll see the red message **"Please provide a more detailed reason (min 10 chars)"** under the field.
4. If you leave it blank, you'll see **"Reason is required"**.

### Step 7: Submit

1. Click the **Create Lab Order** button at the bottom right of the dialog.
2. While the order is being created, the button shows a spinner and the text **"Creating Order..."**.
3. On success a green toast appears: **"Lab test order created successfully"**. The dialog closes, and the new test appears in the patient's tests list.

### Step 8: Cancel if needed

Click **Cancel** at the bottom of the dialog at any time to close it without saving.

### Common problems while ordering a lab test

| Toast | What it means | What to do |
|---|---|---|
| **"Please check your input"** + **"Please enter the test name when selecting 'Other'."** | You picked **Other** but did not type a custom test name. | Fill in the **Specify Test Name** field. |
| **"Reason is required"** | The reason field is empty. | Type at least 10 characters. |
| **"Please provide a more detailed reason (min 10 chars)"** | The reason is too short. | Add more detail. |
| **"Failed to create lab test order"** | The server rejected the request. | Check your internet, then try again. If it persists, contact your administrator. |
| **"The selected visit could not be found."** | The visit was deleted or is no longer valid. | Refresh the page and start a new visit. |

---

## 7. Scenario: Ordering an Imaging Test (Chest X-Ray / CT Scan)

Just like lab tests, the patient must have an in-progress visit.

### Step 1: Open the Order Imaging Test dialog

1. Sidebar > **Manage Patients** > **View Details** on the patient.
2. Click the **Visits** tab.
3. In the in-progress visit's row, click **Order Test**, then choose **Imaging Test** (or click **Order New Test** from the **Tests** tab).
4. The **Create Imaging Test Order** dialog opens with the description **"Fill out the form to order a new Imaging test"**.

### Step 2: Confirm the IDs

`Patient ID` and `Visit ID` are auto-filled and grayed out.

### Step 3: Choose the imaging test type

1. Click the **Imaging Test Type *** dropdown.
2. Pick one of:
   - **Chest X-Ray**
   - **CT Scan**

### Step 4: Investigation Required (optional)

1. Click in the **Investigation Required** field.
2. Type the body part to be examined, for example `Chest, both lung fields`.

### Step 5: Patient Mobility

This tells the radiology team how the patient should be transported. Click the **patient_mobility *** dropdown and pick one — the default is **Walking**.

| Option | Use when |
|---|---|
| **Walking** | The patient can walk to the radiology department on their own. |
| **Chair** | The patient needs a wheelchair. |
| **Stretcher** | The patient must be moved on a stretcher (cannot sit up). |
| **Bedside** | The imaging must come to the patient's bed (the patient cannot be moved). |

### Step 6: Provisional Diagnosis

1. Click in the **Provisional Diagnosis *** text area.
2. Type your initial clinical impression — at least **10 characters**. Example: `Suspected pulmonary tuberculosis with possible cavitation`.
3. Less than 10 characters shows the red error **"Please provide a more detailed reason (min 10 chars)"**.

### Step 7: Clinical Notes (optional)

1. Click in the **Clinical Notes** text area.
2. Type any extra context the radiologist needs, for example: `Patient on second-line MDR-TB regimen, 4 weeks in.`

### Step 8: Submit

1. Click **Create Imaging Order**.
2. The button shows **"Creating Order..."** with a spinner while it processes.
3. On success a green toast appears: **"Imaging test order created successfully"**. The dialog closes.

### Common problems

| Toast | What it means | What to do |
|---|---|---|
| **"Reason is required"** | Provisional Diagnosis is blank. | Fill it in. |
| **"Please provide a more detailed reason (min 10 chars)"** | Provisional Diagnosis is too short. | Add more detail. |
| **"Failed to create imaging test order"** | The server rejected the request. | Check your internet and try again. |

---

## 8. Scenario: Adding Medical History (Enhanced Medical History form)

This page opens automatically right after you register a new patient. You can also reach it from the patient overview to update the history later.

**URL:** `/doctor/patients/enhanced-medical-history/[patientId]`

### Section 1: Physical Measurements

1. **Height** — type the patient's height in centimeters. Decimals are allowed (for example `170.5`). The valid range is **30 to 250 cm**.
   - If you type below 30 you'll see **"Height must be at least 30 cm"**.
   - If you type above 250 you'll see **"Height must be less than 250 cm"**.
   - If you leave it blank you'll see **"Please enter the patient's height"**.
2. **Weight** — type the weight in kilograms. Decimals are allowed (for example `70.5`). The valid range is **2 to 300 kg**.
   - Below 2 kg: **"Weight must be at least 2 kg"**.
   - Above 300 kg: **"Weight must be less than 300 kg"**.
   - Blank: **"Please enter the patient's weight"**.

### Section 2: HIV Status

1. Pick **NEGATIVE** or **POSITIVE**. This is required.

### Section 3: TB History

For each question below, click either **Yes** or **No**. The first question is the most important — every other question is optional but recommended.

1. **Has this patient ever been diagnosed with TB?** — required. Pick **Yes** or **No**. If you skip it you'll see **"Please select Yes or No"**.
2. If you picked **Yes**, the **Previous TB medications** multi-select becomes required. Click it and pick all that apply: **Rifampicin**, **Isoniazid**, **Pyrazinamide**, **Ethambutol**, **Streptomycin**.
3. **Spent time with active TB contact?** — Yes/No.
4. **Had a TB skin test?** — Yes/No.
5. **Had a TB blood test?** — Yes/No.
6. **Coughing for two weeks?** — Yes/No.
7. **Persistent fevers for two weeks?** — Yes/No.
8. **Noticeable weight loss (more than 3 kg)?** — Yes/No.
9. **Excessive night sweats for three weeks?** — Yes/No.
10. **Child contact with pulmonary TB or chronic cough?** — Yes/No (only shown for female patients).

### Section 4: Body Transplant & Other Conditions

1. **Had a body transplant?** — Yes/No.
2. **Has diabetes?** — Yes/No.
3. **Diagnosed with neck or head cancer?** — Yes/No.

If you skip any of these, you'll see **"Please choose Yes or No for this field."**

### Section 5: Symptoms

Tick the checkbox next to every symptom that applies:

- `Cough`, `Fever`, `Night Sweats`, `Chest Pain`, `Dyspnea`, `Chills`, `Weight Loss`, `No Appetite`, `Weakness/Fatigue`, `Coughing up blood/sputum`.

Then:

1. **Temperature** — type the patient's temperature in degrees Celsius. Valid range: **30 to 43 °C**.
   - Below 30: **"Temperature is too low (min 30°C)"**.
   - Above 43: **"Temperature is too high (max 43°C)"**.
   - Blank or non-numeric: **"Please enter a valid temperature"**.
2. **Others** — type any unlisted symptoms here as free text.

### Section 6: Medications

1. **Previous Medications** — multi-select. Click each medication the patient has previously taken.
2. **Consumed antibiotics in the last 6 months?** — Yes/No.
3. **Time first symptom started** — click the date picker and pick the date the patient first noticed symptoms. The date cannot be in the future and cannot be more than 2 years ago.
   - Future date: **"Date cannot be in the future"**.
   - Older than 2 years: **"Date seems too far in the past"**.
4. **Allergies** — free text. Type any allergies, or leave blank.

### Section 7: Patient Type & Risk Factors

1. **Patient Type** — pick one from the dropdown. Required.
2. **Risk Group** — tick every box that applies:
   - `Allergies`, `Consumes Alcohol`, `Cough`, `Diabetic`, `Fisher Folk`, `Healthcare Worker`, `Medication`, `Mentally Ill`, `Miner`, `Pregnant` (only shown for female patients), `Prisoner`, `Refugee`, `TB Contact`, `Tobacco User`, `Uniformed Personnel`.
3. **Others** — type any unlisted risk factors.

### Saving

1. Click the **Save** button (or **Update** if you are editing an existing record).
2. While saving, the button is disabled.
3. On success, a green toast confirms the save and you are taken back to the patient overview.
4. If validation fails, the page scrolls to the first error and the field shows the red message described above.

---

## 9. Scenario: Prescribing medication

You can only prescribe medication for a visit that is **In Progress**.

### Step 1: Find the active visit

1. Sidebar > **Manage Patients** > **View Details** on the patient.
2. Click the **Visits** tab.
3. Find the row with the amber **In Progress** badge.

### Step 2: Open the prescription page

1. In that row, click the **Prescribe Medication** button in the Actions column.
2. You are now at `/doctor/patients/prescribe-medication/[visit_id]`.
3. The page shows a header **Prescribe Medication** with the subtitle **"Create a prescription for this patient visit"**, plus a panel showing the visit's details (visit type, status, date, notes, and any tests ordered).

If the page shows **Visit Not Found**, the visit was deleted or you do not have access. Click **Back to Dashboard** and start over.

### Step 3: Fill in the prescription form

1. **Medication Name** — type the drug name (for example `Isoniazid`). Must be 2 to 200 characters.
2. **Dosage** — type the dose (for example `300mg`). 1 to 100 characters.
3. **Frequency** — type how often (for example `Once daily` or `Twice daily`). 1 to 100 characters.
4. **Duration** — type the length of treatment (for example `14 days` or `6 months`). 1 to 100 characters.
5. **Instructions** — type clear patient instructions (for example `Take with food. Avoid alcohol. Report any rash immediately.`). 5 to 500 characters.

### Step 4: Decide whether to close the visit

- If this is your only prescription for this visit and you are done with the visit, tick the **Close this visit** checkbox.
- If you plan to add more prescriptions, leave it unticked. You can come back and add more.

### Step 5: Submit

1. Click **Prescribe Medication** (or **Update Prescription** if you are editing an existing one).
2. While submitting, the button is disabled.
3. On success, a green toast confirms the prescription was saved. If you ticked **Close this visit**, the visit's status changes to **Completed** and you can no longer add prescriptions to it.

### Step 6: Verify it appears

1. Click the **Prescriptions** tab on the patient page.
2. The new prescription appears as a card showing the medication name (large, bold), the visit status, the prescribed date, and all the dosage details.
3. While the visit is still in progress you'll see an **Edit** button on the card. Once the visit is completed, the button changes to **Cannot Edit**.

---

## 10. Scenario: Reviewing test results

### Finding a completed test

1. From the sidebar, click **Test Orders**. You are now at `/doctor/test-orders`.
2. Pie charts at the top show the breakdown of all tests, lab tests, and imaging tests by status. Click **Refresh** to reload them.
3. Below the charts are two tabs: **Lab Tests** and **Imaging Tests**.

### Reviewing a lab test

1. Click the **Lab Tests** tab.
2. Sort by `Status` by clicking the column header until **COMPLETED** rows are at the top.
3. Find the test you want and click **View Details** in the Actions column.
4. You are now on `/doctor/lab-test/[id]`.
5. The page shows:
   - **Test Information**: test name, type, status badge, ordered date and time.
   - **Patient & Visit**: patient name, visit type, visit status, visit date.
   - **Reason for Examination**: the clinical justification you entered when you ordered the test.
   - **Results**: the laboratory's reported result, if available. If the lab has not uploaded a result yet, this section is empty.

### Reviewing an imaging test

1. Click the **Imaging Tests** tab on the test orders page.
2. Find the completed imaging test and click **View Details**. You are now on `/doctor/imaging-test/[id]`.
3. The page shows:
   - **Test Information**: test name, type, status, ordered date.
   - **Patient & Visit**: patient name, visit type, status, date.
   - **Provisional Diagnosis**, **Clinical Notes**, **Patient Mobility**, **Investigation Required** — everything you entered when ordering.
   - **Images**: thumbnails of every image uploaded by the radiologist. Click any thumbnail to open the full-size **Image Viewer** page (`/doctor/view-image/[imageId]`). From the viewer you can zoom and pan.
   - **Radiology Report**: the radiologist's narrative report, if completed.

---

## 11. Scenario: Using AI Insights / MDR-TB prediction

The system can predict whether a patient is likely to respond to MDR-TB treatment. The prediction is most useful from the **2-month** follow-up visit onward, because it uses lab and imaging results from that point in treatment.

### Step 1: Open the AI Insights tab

1. Sidebar > **Manage Patients** > **View Details** on the patient.
2. Click the **AI Insights** tab (lightbulb icon).

### Step 2: Pick a visit

1. Click the visit dropdown.
2. Pick a visit. Each option is shown as `[Date] - [Visit Type] ([Status])`.
3. The system fetches and displays the prediction.

### Step 3: Read the result

There are two possible outcomes:

- **Green banner — "Will likely respond to treatment"**: the model thinks the patient will respond well. The page also shows the **MTBC Negative probability** as a percentage.
- **Red banner — "Not likely to respond to treatment"**: the model thinks the patient is unlikely to respond. The page shows the **MTBC Positive probability** as a percentage.

The probability is the model's confidence. Treat it as a clinical decision support tool, **not** a final diagnosis.

### Step 4: Handle error states

| Message | What it means | What to do |
|---|---|---|
| **"Incomplete Medical History"** | The patient's medical history is missing fields the model needs. | Click the link in the message to open the medical history page and fill in the missing fields. |
| **"No prediction data available"** | The model has not yet generated a prediction for this visit. | Click **Refresh Analysis** to retry. |

---

## 12. Common error messages — plain English meaning

The system shows error toasts at the top-right of the screen. Most messages now use plain English. The full mapping lives in `src/utils/networkUtils.ts` in the `humanizeBackendMessage` function. The most common ones are:

| Toast title and description | What it really means | What to do |
|---|---|---|
| **"Please check your input"** + **"Please enter the test name when selecting 'Other'."** | When ordering a lab test, you picked **Other** but did not fill in the **Specify Test Name** field. | Type a test name (e.g. `AFB Smear`) and submit again. |
| **"Please check your input"** + **"Please choose Yes or No for this field."** | A required Yes/No question (radio button) was left blank. | Scroll up, find the question, click **Yes** or **No**, then resubmit. |
| **"Please check your input"** + **"Please enter a valid number."** | A number field is empty or contains letters. | Type a valid number (digits only, decimals allowed where supported). |
| **"Please check your input"** + **"This field is required."** | A required text field is empty. | Find the highlighted field and fill it in. |
| **"Please check your input"** + **"A required selection is missing. Please pick an option from the list."** | You forgot to pick something from a dropdown. | Open the dropdown and select an option. |
| **"Your account isn't fully set up yet. Please contact your administrator."** | Your user account exists but is not linked to a doctor profile. | Contact your facility administrator to complete your setup. |
| **"We couldn't find your doctor profile. Please contact your administrator."** | Same as above — the system cannot find your doctor record. | Contact your facility administrator. |
| **"We couldn't load your facility information. Please try again."** | The backend couldn't fetch your facility's details. | Refresh. If it persists, contact your administrator. |
| **"No patients are linked to your account yet."** | You have no assigned patients. | Wait for your administrator to assign some, or register your own from **Manage Patients > Register New Patient**. |
| **"The patient record could not be found."** | The patient was deleted or you don't have access. | Go back to the patient list and try a different patient. |
| **"The selected visit could not be found."** | The visit was deleted or never saved properly. | Refresh the page and try creating a new visit. |
| **"Network Error"** + **"Please check your internet connection and try again."** | Your device is offline. | Reconnect to Wi-Fi or mobile data and try again. |
| **"Unauthorized - Please login again"** | Your session has expired or your password changed. | Click **Log Out** and log back in. |
| **"Access Denied"** + **"You don't have permission to perform this action."** | Your account does not have the required permission. | Contact your administrator. |
| **"Not Found"** | The thing you tried to open does not exist anymore. | Go back to the previous page and try again. |
| **"Service Unavailable"** + **"The service is temporarily unavailable. Please try again later."** | The backend is down for maintenance. | Wait a few minutes and try again. |
| **"Something went wrong"** + **"We're having trouble right now. Please try again in a moment."** | An unexpected server error. | Try again. If it keeps happening, contact your administrator. |

---

## 13. Tips & gotchas

- **Visit times are now in your local timezone.** Earlier versions showed times offset by 3 hours. If you ever see a visit dated in the future or far in the past, refresh the page.
- **Shimmer placeholders mean the page is loading.** When you see grey animated rectangles in tables and cards, the system is fetching data — wait a few seconds.
- **On a phone or tablet, tables become cards.** All the same information is there, just rearranged so you can scroll vertically.
- **Empty lists show a friendly illustration.** If the patients table, tests table, or visits table is empty, you will see an illustration with a hint such as **"No patients are linked to your account yet."** That's not an error — it's just empty.
- **You cannot order tests or prescribe without an active visit.** If the **Order New Test** or **Prescribe Medication** button is greyed out, you have no in-progress visit. Create one first (see [Section 5](#5-scenario-starting-a-new-visit-for-a-patient)).
- **You cannot edit prescriptions on completed visits.** Once you tick **Close this visit** and submit, the prescriptions on that visit are locked. The Edit button changes to **Cannot Edit**.
- **The "Other" test type always needs a custom name.** The system will not accept the order until you fill the **Specify Test Name** field.
- **Weight and height accept decimals.** `70.5 kg` and `170.5 cm` are valid.
- **Temperature must be between 30°C and 43°C.** Anything outside that range is rejected.
- **The medical history "Ever diagnosed with TB?" question controls the rest.** If you answer **Yes**, the **Previous TB medications** multi-select becomes required.
- **Dates of first symptoms cannot be in the future or older than 2 years.** Use the date picker, not free text.
- **Refreshing the page is safe.** It will not lose any data you have already saved. It only loses what you have typed in an open form but not yet submitted.

---

*For general navigation, login, and settings instructions that apply to every role, see the [General System Guide](./00-general-system-guide.md).*
