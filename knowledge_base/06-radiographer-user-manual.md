# Radiographer User Manual

This manual is written as a step-by-step recipe for radiographers using the DSI MDR-TB management web app. Follow the numbered steps in the order shown. Bold text indicates a button or link to click. `Code style` indicates a field label as it appears on screen. Quoted text is the exact wording you will see in toasts or messages.

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Dashboard Tour](#2-dashboard-tour)
3. [Scenario: Viewing all imaging test orders](#3-scenario-viewing-all-imaging-test-orders)
4. [Scenario: Opening an imaging test order](#4-scenario-opening-an-imaging-test-order)
5. [Scenario: Creating an imaging test record (before upload)](#5-scenario-creating-an-imaging-test-record-before-upload)
6. [Scenario: Uploading an image (single file)](#6-scenario-uploading-an-image-single-file)
7. [Scenario: Re-uploading or adding more images](#7-scenario-re-uploading-or-adding-more-images)
8. [Scenario: Viewing uploaded images](#8-scenario-viewing-uploaded-images)
9. [Common error messages — plain English meaning](#9-common-error-messages--plain-english-meaning)
10. [Tips and gotchas](#10-tips-and-gotchas)

---

## 1. Getting Started

### 1.1 Logging in

1. Open your web browser and go to the DSI MDR-TB application URL provided by your facility administrator.
2. On the login screen, type your email address into the `Email` field.
3. Type your password into the `Password` field.
4. Click the **Login** button.
5. If your credentials are correct, you will be taken to your Radiographer Dashboard at `/radiographer`.

### 1.2 The landing page

After login, you land on the **Dashboard**. The page title at the top of the browser tab will read "Dashboard". The left sidebar shows three main menu items:

| Menu item | Where it takes you |
|-----------|--------------------|
| **Dashboard** | `/radiographer` — overview metrics and recent activity |
| **Imaging Tests** | `/radiographer/imaging_tests` — full list of all imaging test orders |
| **Settings** | `/radiographer/settings` — change your password and profile |

At the bottom of the sidebar is a **Log Out** option.

### 1.3 Logging out

1. Click **Log Out** at the bottom of the left sidebar.
2. You will be returned to the login screen.
3. Always log out when you leave a shared workstation.

### 1.4 Resetting your password

1. On the login screen, click the **Forgot Password?** link below the password field.
2. Enter the email address linked to your radiographer account.
3. Submit the form. You will receive an email with a password reset link.
4. Open the email, click the link, and choose a new password.
5. Use your new password to log back in.

If you do not receive the email, contact your facility administrator — they can reset your password from the admin panel.

---

## 2. Dashboard Tour

URL: `/radiographer`

The Dashboard is the first thing you see after login. It is divided into three sections from top to bottom: **Overview metrics**, **Recent Ordered Imaging Tests**, and **Recent Imaging Tests**.

### 2.1 Overview metrics (the four cards at the top)

You will see four colored cards in a row (they stack vertically on a phone). Each shows a number and a label.

| Card | Color stripe | What the number means |
|------|--------------|------------------------|
| `Pending Orders` | Blue | Imaging orders that doctors have placed but no radiographer has acted on yet. This is your work queue. |
| `Awaiting Analysis` | Yellow | Imaging tests where you have already uploaded images, and they are waiting for a radiologist to write the report. |
| `Completed Orders` | Red | Tests that have a finished radiology report. The full cycle (order → image → report) is done. |
| `My Tests` | Green | The total number of imaging tests you personally have performed. This is a lifetime counter. |

While the dashboard is loading you will see four shimmering grey placeholder cards. They are replaced with the real numbers within a second or two.

### 2.2 Recent Ordered Imaging Tests (middle section)

This section shows the three most recent imaging test orders sent to the radiology department. The number of total orders is shown next to the heading as a small badge (for example, "12 tests").

On a desktop screen you see a table with these columns:

| Column | Meaning |
|--------|---------|
| `Patient` | Patient's full name |
| `Doctor` | Name of the doctor who ordered the test |
| `Test Type` | What was ordered (for example, Chest X-Ray, CT Scan) |
| `Status` | Color-coded badge — see the status table in section 3.2 |
| `Patient Mobility` | How the patient can be moved (Walking, Chair, Stretcher, Bedside) |
| `Time` | Relative time — for example, "2 hours ago" |
| `Actions` | Buttons for what you can do next |

On a phone or tablet, the same information is shown as stacked cards instead of a table.

The **Actions** column shows:

- **View Order** (blue, always visible) — opens the full order details page.
- **Create Imaging Test** (green, only visible when status is `ORDERED`) — jumps directly to the create-and-upload page.

### 2.3 Recent Imaging Tests (bottom section)

This is a second list — but this one shows tests **you have already performed** (not orders waiting for you). Columns:

| Column | Meaning |
|--------|---------|
| `Test Type` | The body part recorded when you created the test |
| `Patient Name` | Patient's full name |
| `Status` | "Completed" if a radiologist has written a report, otherwise "Awaiting Analysis" |
| `Total Images` | How many image files are attached |
| `Time` | Relative time since the test was performed |
| `Actions` | **View Details** button |

If either section has no entries you see a friendly empty-state panel ("No imaging test orders" or "No imaging tests").

---

## 3. Scenario: Viewing all imaging test orders

Use this when you want to see the full list (not just the three most recent on the dashboard).

### 3.1 Where the list lives

1. In the left sidebar, click **Imaging Tests**.
2. You arrive at `/radiographer/imaging_tests`. The page title shows "Imaging Test Orders" with the test-tube icon and a count badge (for example, "8 tests").

### 3.2 What the status indicators mean

Every order has one of three statuses, shown as a colored pill:

| Status pill | Color | What it means | What you should do |
|-------------|-------|----------------|---------------------|
| `Ordered` | Blue | The doctor has placed the order. Nothing has been done yet. | Perform the imaging test, then create the test record and upload images. |
| `Awaiting Analysis` | Yellow | You (or another radiographer) have already performed the test and uploaded images. A radiologist still has to read them. | Nothing — the radiologist takes over. |
| `Completed` | Green | The radiologist has finished the report. | Nothing — the workflow is closed. |

### 3.3 Filtering by status

Below the page heading you will see four pill-shaped filter buttons:

1. **all** — shows every order regardless of status (this is the default).
2. **ordered** — shows only orders that need your action.
3. **awaiting analysis** — shows tests waiting for the radiologist.
4. **completed** — shows finished tests.

Click any pill to apply that filter. The active filter is highlighted in dark blue with white text.

### 3.4 Searching

To the right of the heading is a search input with the placeholder text "Search test type or status...". Type any part of a test type (for example, `chest`) or a status (for example, `ordered`). The list filters as you type. Note: this search box matches **test type** and **status** text — it does not search by patient name.

### 3.5 Mobile cards versus desktop table

- **Desktop / wide screen**: orders display as a horizontal table with all seven columns described in section 2.2.
- **Phone / narrow screen**: each order becomes a stacked card showing Patient, Doctor, Test Type, Status, Mobility, Time, and the same two action buttons. Scroll vertically to see more.

The switch between table and card layout happens automatically based on your screen width.

---

## 4. Scenario: Opening an imaging test order

Use this when you want to read all the clinical detail about a single order before performing the imaging test.

### 4.1 Click flow

1. From the **Dashboard** or **Imaging Tests** list, find the order you want.
2. Click the blue **View Order** pill in the **Actions** column.
3. You arrive at `/radiographer/imaging_test/{id}` (the order details page). The browser tab title becomes "Imaging Test Order Details".

### 4.2 What you see on the order details page

The page is laid out in three areas: a dark blue header, a two-column information card, and a lower images section with a sidebar for the ordering doctor.

#### Dark blue header banner

- The title "Imaging Test Order Details".
- The patient's full name underneath.
- A status badge on the right (green for `Completed`, yellow for `Awaiting Analysis`, blue for `Ordered`).
- A green **Create Imaging Test** button (only when the status is `Ordered`).

#### Patient Information (left column of the white card)

| Field | Description |
|-------|-------------|
| `Full Name` | First and last name |
| `Age` | Patient's age in years |
| `Gender` | Female or Male |
| `National ID` | National identification number, or "N/A" |
| `Phone Number` | Contact phone, or "N/A" |
| `Email` | Email address, or "N/A" |

If an address is on file you also see `Country`, `District`, `Region`, `County`, `Sub County`, `Parish`, and `Village` (only those fields that are filled).

#### Test Order Details (right column, top half)

| Field | Description |
|-------|-------------|
| `Test Type` | Chest X-Ray, CT Scan, etc. |
| `Body Part` | The body part you typed when creating the imaging test (only after creation) |
| `Patient Mobility` | Walking / Chair / Stretcher / Bedside |
| `Ordered Date` | When the doctor placed the order, in your local time |
| `Performed Date` | When you uploaded the test, or "Not yet performed" |

#### Clinical Information (right column, bottom half)

| Field | Description |
|-------|-------------|
| `Clinical Notes` | Free-text notes the ordering doctor wrote |
| `Investigation Required` | Specific investigation the doctor wants |
| `Provisional Diagnosis` | The doctor's working diagnosis |

If the doctor left a field blank you see "No clinical notes provided", "Not specified", or "Not provided" — that just means the doctor did not fill it in.

#### Ordering Doctor sidebar (right side, below the main card)

| Field | Description |
|-------|-------------|
| `Doctor Name` | Name of the doctor who placed the order |
| `Phone` | Doctor's phone (only shown if available) |
| `Email` | Doctor's email (only shown if available) |

Use this if you need to call the doctor for clarification before imaging.

---

## 5. Scenario: Creating an imaging test record (before upload)

This is the action you take after the patient has actually been imaged in the radiology suite. It creates the database record for the test and uploads the first image at the same time.

### 5.1 Starting the create flow

You can reach the create page from three places:

- **From the Dashboard list**: click the green **Create Imaging Test** pill in the Actions column.
- **From the Imaging Tests list**: click the same green pill.
- **From the Order Details page**: click the green **Create Imaging Test** button in the dark blue header, or scroll to the empty Patient Images box and click **Create Imaging Test & Upload Image**.

All three routes take you to `/radiographer/create_imaging_test/{id}`.

### 5.2 Filling in the form

The page heading is "Create Imaging Test". You will see two fields below it.

1. **Body Part** — required text field.
   - Type the anatomical body part you imaged (for example, `Chest`, `Left Wrist`, `Lumbar Spine`).
   - This field is mandatory. The submit button stays disabled until you type something.
2. **Upload Medical Image** — required file picker (covered in section 6).

### 5.3 Accepted file types

The system accepts:

- `JPG` / `JPEG`
- `PNG`
- `DICOM` (`.dcm`) — the standard medical imaging format

Maximum file size: **100 MB** per file.

---

## 6. Scenario: Uploading an image (single file)

This is the second half of the create flow described in section 5. You arrive here on the same `/radiographer/create_imaging_test/{id}` page after typing the body part.

### 6.1 Selecting a file

Below the body-part field, the heading "Upload Medical Image" is followed by a large dashed rectangle with a cloud icon and the text "Click or drag & drop to upload".

You can choose your file in two ways.

**Option A — drag and drop:**

1. Open your computer's file explorer and find the image file.
2. Drag the file over the dashed rectangle.
3. The rectangle turns blue, the icon changes to a hand pointer, and the text becomes "Drop file here".
4. Release the mouse button to drop the file.

**Option B — click to browse:**

1. Click anywhere inside the dashed rectangle.
2. Your operating system's file picker opens.
3. Navigate to the image file and click **Open**.

### 6.2 What you see after selection

- **JPG or PNG**: the rectangle is replaced with a thumbnail preview of the image.
- **DICOM**: instead of a preview you see a file icon, the file name, and the message "Preview not available for DICOM files". A small toast at the top says "Selected DICOM file: filename.dcm". This is normal — DICOM files cannot be rendered in a web browser preview, but they will still upload correctly.

A red **Remove** button appears in the top-right of the preview area. Click it to clear the file and pick a different one.

### 6.3 Maximum file size

If your file is larger than **100 MB**, the form will reject it with the message "Max file size is 100MB." Use a smaller export from your imaging machine, or compress the file before upload.

### 6.4 Submitting

1. Confirm both `Body Part` is typed and an image is selected. The big blue **Create Test & Upload Image** button is now enabled.
2. Click **Create Test & Upload Image**.
3. A full-screen animated loader takes over the page. It runs in two stages:
   - Stage 1: "Creating imaging test" — the test record is being saved. The progress bar fills toward 20%.
   - Stage 2: "Uploading medical image" — the image file is being transferred. The progress bar climbs from 20% to 100%.
4. When stage 1 finishes, a green toast appears at the top of the screen reading "Imaging test created. Now uploading the image."
5. When stage 2 finishes successfully, a second green toast reads "Imaging Test Created Successfully".

### 6.5 What happens after a successful upload

After about one second the loader disappears and you are automatically taken to the **Imaging Test Order Details** page at `/radiographer/imaging_test_details/{new_test_id}`.

On that details page you will see **all** of the following — both the doctor's original clinical fields and your new imaging data — together on one screen:

- The patient's full name, age, gender, contact info, and address (from the original order)
- `Test Type` (Chest X-Ray, CT Scan, etc., from the doctor's order)
- `Body Part` (the value you just typed)
- `Patient Mobility` (from the doctor's order)
- `Clinical Notes` (from the doctor)
- `Investigation Required` (from the doctor)
- `Provisional Diagnosis` (from the doctor)
- `Ordered Date` and `Performed Date`
- The new image card under **Patient Images**, with **View Image** link

If any of those clinical fields look empty, that simply means the doctor did not fill them in when placing the order — it does **not** mean the data was lost. The system always merges the doctor's order data with your imaging test data so you see one complete picture.

### 6.6 What happens if the upload fails

If something goes wrong, the loader closes and a red toast appears with one of these messages:

- "Failed to upload image." — generic upload failure. Try again.
- "Failed to create imaging test." — the test record was not saved at all. Try again or contact IT.
- A specific validation message from the server (for example, file too large, invalid file type).

The form keeps your body-part text and selected file so you can retry without re-entering everything.

---

## 7. Scenario: Re-uploading or adding more images

Sometimes you need to add a second view (for example, both AP and lateral chest views) or replace a bad image. Use this flow.

### 7.1 Where to click

1. Open the imaging test details page (`/radiographer/imaging_test_details/{id}`) for the test you want to add an image to.
2. Look in the address bar — note the test ID number after `imaging_test_details/`.
3. Manually navigate to `/radiographer/upload_image/{id}` using that same test ID. (This route is the dedicated additional-image uploader.)

The page heading reads "Upload Medical Image".

### 7.2 The upload flow

The form on this page is the same as the one in section 6, **without** the body-part field (because the body part was set when the test was first created).

1. Drag and drop the new file onto the dashed rectangle, OR click the rectangle and browse.
2. The same preview behavior applies: image thumbnail for JPG/PNG, file icon for DICOM.
3. Click the **Remove** button to discard the selection and pick again.
4. When you are ready, click the blue **Upload Image** button.
5. The loader shows "Uploading medical image" with a progress bar.
6. On success, a green toast reads "Image uploaded successfully!".
7. After about one second you are sent back to the imaging test details page, which automatically refreshes both the imaging-test list and the order list so the latest data is visible.
8. The new image will appear in the **Patient Images** grid alongside any earlier images.

### 7.3 If something fails

Same error toasts as section 6.6 — "Failed to upload image. Please try again." or a specific server message.

---

## 8. Scenario: Viewing uploaded images

### 8.1 Finding the images on the details page

1. Open an imaging test that has at least one image (status is `Awaiting Analysis` or `Completed`).
2. Scroll down to the **Patient Images** section. You will see a count badge ("3 image(s)", for example).
3. Each image is shown as a card with:
   - "Image 1", "Image 2", etc.
   - `Upload Date` — the timestamp shown in your local time
   - `Patient` — patient name
   - A blue **View Image** button at the bottom of the card.

### 8.2 Opening the image viewer

1. Click **View Image** on the card you want to inspect.
2. You arrive at `/radiographer/view-image/{imageId}`.
3. The image is displayed with viewer controls. For DICOM files, the dedicated DICOM viewer renders the pixel data. For JPG/PNG, a standard image viewer is used.
4. Common controls in the toolbar include zoom in/out, pan, rotate, brightness/contrast, invert, ruler/measurement, grid overlay, fullscreen, and annotation. Hover over any toolbar button to see its tooltip.
5. To return to the test details page use your browser's **Back** button or click the breadcrumb at the top of the viewer.

### 8.3 Where the radiology report appears

The radiologist's written report becomes visible **on the same imaging test details page** once the radiologist completes their analysis.

1. Open the test details page after the radiologist has finished.
2. The status badge in the dark blue header changes from yellow `Awaiting Analysis` to green `Completed`.
3. A new section displaying the report text appears below the Patient Images grid.
4. As a radiographer you cannot edit the report — you can only read it.

If the status is still yellow, you will see "Awaiting Radiologist Analysis" in the empty area where the report would go. There is nothing for you to do at that point.

---

## 9. Common error messages — plain English meaning

The system translates raw backend errors into friendlier wording before showing them. Here are the ones you are most likely to see as a radiographer.

### 9.1 Upload-specific errors

| Toast text you see | What it actually means | What to do |
|--------------------|------------------------|------------|
| "Failed to upload image." | The file did not reach the server. | Check your internet connection and try again. |
| "Failed to upload image. Please try again." | Same as above, generic. | Retry once. If it keeps failing, try a smaller file. |
| "Failed to create imaging test." | The test record itself could not be saved. The image was not uploaded. | Confirm the body part field is filled. Try again. |
| "Max file size is 100MB." | The file you picked is bigger than 100 MB. | Export a smaller version from your imaging machine, or compress before upload. |
| "Image file is required" | You clicked submit without picking a file. | Click the dashed upload area and choose a file. |
| "Body Part is required" | You clicked submit without typing in the body part. | Type the body part name and try again. |
| "Selected DICOM file: filename.dcm" | This is not an error — it is a blue info toast confirming the system recognized your DICOM file. | Continue with submission. |
| "Imaging test created. Now uploading the image." | This is a green progress toast (not an error). | Wait for the second toast. |
| "Imaging Test Created Successfully" | Green success toast — everything worked. | You will be redirected automatically. |
| "Image uploaded successfully!" | Green success toast for additional uploads. | You will be redirected automatically. |

### 9.2 General system errors

| Toast title | Description text | What it means | What to do |
|-------------|------------------|---------------|------------|
| "Please check your input" | Various — depends on the field | The server rejected what you submitted because a field was missing or in the wrong format. The description tells you which field. | Re-read the form, fix the highlighted field, and submit again. |
| "Not Found" | "The requested information could not be found." | The order or test you tried to open does not exist (it may have been deleted, or the URL is wrong). | Go back to the Imaging Tests list and pick a current item. |
| "Access Denied" | "You don't have permission to perform this action." | You are logged in but your radiographer role does not allow this action. | Contact your administrator if you believe you should have access. |
| "Something went wrong" | "We're having trouble right now. Please try again in a moment." | The server returned a 500 error. | Wait a minute, then retry. If it persists, contact IT. |
| "Service Unavailable" | "The service is temporarily unavailable. Please try again later." | The server is down or restarting. | Wait several minutes, then retry. |
| "Network Error" | (no description) | Your computer cannot reach the server. | Check your internet/Wi-Fi connection. |
| "Session Expired" or being kicked back to login | — | You have been inactive for too long, or your token expired. | Log in again with your email and password. |
| "This field is required." | — | One of the form fields is empty. | Fill it in. |
| "Please enter a valid number." | — | A numeric field has letters in it. | Type digits only. |

### 9.3 Field highlight errors

If a form field is invalid, a small red message appears directly under the field (not as a toast). Examples: "Body Part is required", "Image file is required". Fix the field and the red message disappears.

---

## 10. Tips and gotchas

### 10.1 DICOM previews

- DICOM files (`.dcm`) **do not show a thumbnail** in the upload area before you submit. This is normal — web browsers cannot render DICOM pixel data without a special viewer. You will see a file icon and the file name instead. The file uploads correctly, and once it is on the server you can open it in the dedicated image viewer.

### 10.2 All times are in your local timezone

- Every date and time on the application (`Ordered Date`, `Performed Date`, `Upload Date`, "2 hours ago", etc.) is shown in **your local time**, not UTC. There is no offset to remember. If a record was created at 14:30 your local time, you will see 14:30.

### 10.3 Loading placeholders

- When data is loading, the dashboard cards and tables show **shimmering grey placeholders**. This is not an error — it just means the page is still fetching data. Wait one or two seconds.

### 10.4 Mobile cards

- On a phone, every table in the app automatically becomes a stack of cards. You do not lose any information — it is just laid out vertically. You may need to scroll down further to see all the entries.

### 10.5 Auto-refresh after upload

- After a successful image upload, the system **automatically refreshes both the imaging test list and the imaging test order list** in the background. This means when you land on the details page after upload, the latest data is already there. You do **not** need to press F5 or click a refresh button.

### 10.6 Clinical fields are always preserved

- After you upload an image, the test details page merges the doctor's original order data (test type, mobility, clinical notes, provisional diagnosis, investigation required) with your imaging data (body part, performed date, images). You will always see the doctor's notes alongside your work — nothing disappears.
- If a clinical field shows "No clinical notes provided" or "Not specified", that means the doctor left it blank when placing the order. Contact the doctor if you need clarification.

### 10.7 Body part is set once

- The `Body Part` field can only be typed when you first create the imaging test record (section 5). The additional-upload screen (section 7) does not show it again because it belongs to the test, not to each image.

### 10.8 Action buttons appear based on status

- The green **Create Imaging Test** button only appears when the status is `Ordered`. Once you create the test, the status flips to `Awaiting Analysis` and the button disappears from that order — there is nothing left to create.

### 10.9 Searching is by test type and status only

- The search box on the **Imaging Tests** list does **not** match patient names or doctor names. Use the test type (for example, "ct") or the status keyword (for example, "ordered") to filter. To find a patient by name, scroll the list visually or use your browser's Ctrl+F find function on the page.

### 10.10 Always log out on shared workstations

- The app stores your session token in the browser. If you walk away without logging out, the next person can act on patient records under your name. Click **Log Out** in the sidebar before leaving the machine.

---

*For login, password reset, and general settings instructions that apply to every role, see the [General System Guide](./00-general-system-guide.md).*
