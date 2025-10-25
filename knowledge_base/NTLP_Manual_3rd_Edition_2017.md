---
title: "National Tuberculosis and Leprosy Programme (NTLP) Manual — 3rd Edition"
source: "Ministry of Health, Republic of Uganda — NTLP Manual (3rd edition)"
source_url: "https://health.go.ug/sites/default/files/NTLP%20Manual%203rd%20edition_17th%20Aug_final.pdf"


# Manual for Management and Control of Tuberculosis in Uganda (3rd Edition – March 2017)

## structured summary

This top section provides a concise, machine-friendly map of the manual to improve retrieval and chunking for the chatbot. The authoritative, full-text sections follow below (beginning at "SECTION ONE").

- Title: National Tuberculosis and Leprosy Programme (NTLP) Manual — 3rd Edition (March 2017)
- Source: Ministry of Health, Republic of Uganda (see `source_url` in frontmatter)
- Purpose: National guidance on TB and leprosy diagnosis, treatment, prevention, infection control, laboratory services and programme management.

Main chapters (use these as chunking anchors):

- Section 1 — Introduction & NTLP structure
  - Geography, demography, health service delivery, burden of TB/leprosy, NTLP organisation and roles (national → regional → district → HSD → community).

- Section 2 — Tuberculosis (core clinical content)
  - Disease basics (causative organism, transmission, LTBI)
  - Diagnosis (screening, Xpert, microscopy, culture, CXR, histology)
  - Treatment (first-line regimens, dosing, monitoring, adverse effects, adherence/DOT)
  - Preventive therapy (IPT) and target populations
  - Special situations (pregnancy, children, liver/renal disease)
  - Drug-resistant TB (definitions, diagnosis, regimen-building, groups of drugs, monitoring)
  - TB/HIV collaborative activities and TB infection control
  - Laboratory network and M&E indicators

- Section 3 — Leprosy
  - Case finding, classification, MDT, complications, prevention of disability (POD), rehabilitation, monitoring and registers

- Annexes
  - Forms, registers, lab techniques, logistics, supervision tools, treatment support guidance

How to use this file for the chatbot:

- Use the bullets above as high-level retrieval anchors for short answers.
- Use detailed subsections in the full text below for evidence and citations.
- If you want finer-grained chunks, tell me which sections to split (e.g., Diagnosis, Treatment, DR-TB) and I will split them into separate .md files for better vectorization.

---
- **Chest X-ray (CXR)** findings consistent with TB:
  - Cavitation
  - Miliary pattern
  - Pleural effusion
  - Mediastinal lymphadenopathy with lung infiltration
  - Heterogeneous opacities in upper lung zones
- All bacteriologically negative presumptive TB patients should have CXR.
- If CXR is suggestive of TB, start treatment.

### 2.2.4 Histology
- Used for extra-pulmonary TB (e.g., lymphadenitis).
- Characteristic granulomatous inflammation confirms diagnosis.
- Samples obtained via:
  - Fine needle aspiration (lymph nodes)
  - Tissue biopsy (pleura, pericardium, skin, liver, etc.)

### 2.2.5 Standard TB Case Definitions
- **Presumptive TB patient**: Any patient with symptoms/signs suggestive of TB.
- **Bacteriologically confirmed TB patient**: Biological specimen positive by smear, culture, NAAT (e.g., Xpert), or WHO-recommended diagnostics.
- **Clinically diagnosed TB patient**: Not bacteriologically confirmed but diagnosed by clinician based on CXR, histology, or clinical judgment and started on full TB treatment.
  - If later found bacteriologically positive, reclassify as confirmed.

### 2.2.6 Classification of TB Patients
Classification is based on four factors:

#### 1. Site of Disease
- **Pulmonary TB (PTB)**: Involves lung parenchyma or tracheobronchial tree.
  - Includes endobronchial TB (highly infectious; presents with barking cough, wheezing).
- **Extra-pulmonary TB (EPTB)**: Involves organs other than lungs (e.g., pleura, lymph nodes, abdomen, meninges).
- **Note**: Patients with both PTB and EPTB are classified as PTB.

#### 2. History of Treatment
- **New patient**: Never treated or treated <1 month.
- **Previously treated patient**:
  - **Relapse**: Completed treatment, declared cured/completed, now recurrent TB.
  - **Treatment after failure**: Treatment failed in most recent course.
  - **Treatment after loss to follow-up**: Interrupted treatment for ≥2 months.
  - **Other previously treated**: Outcome unknown or undocumented.
- **Note**: New and relapse cases are incident TB cases.

#### 3. HIV Status
- **HIV-positive TB patient**: Positive HIV test at diagnosis or documented in HIV care registers.
- **HIV-negative TB patient**: Negative HIV test at diagnosis.
- **HIV status unknown**: No test result or documentation.
- Patients should be reclassified if HIV status is later determined.

#### 4. Drug Resistance
- **Mono-resistance**: Resistance to one first-line drug.
- **Poly-resistance**: Resistance to >1 first-line drug (not both H and R).
- **Multidrug resistance (MDR-TB)**: Resistance to at least isoniazid and rifampicin.
- **Extensively drug-resistant TB (XDR-TB)**: MDR-TB plus resistance to any fluoroquinolone and at least one second-line injectable (amikacin, capreomycin, kanamycin).
- **Rifampicin-resistant TB (RR-TB)**: Resistance to rifampicin (by phenotypic or genotypic methods), with or without resistance to other drugs.
  - Includes mono-, poly-, MDR-, and XDR-TB with rifampicin resistance.

### 2.2.7 Post-TB Patients
- Patients successfully treated for TB who present later with respiratory symptoms (cough, chest pain, dyspnea, hemoptysis).
- First step: Repeat standard TB evaluation (sputum, CXR).
  - If TB confirmed: treat as retreatment case.
  - If TB excluded: evaluate for post-TB lung disease (e.g., bronchiectasis, COPD, aspergillosis).
- Avoid repeated empirical TB treatment without confirmation.

## 2.3 Treatment of Tuberculosis

### 2.3.1 Anti-TB Medicines
- **First-line drugs** (for drug-susceptible TB):
  - Rifampicin (R)
  - Isoniazid (H)
  - Pyrazinamide (Z)
  - Ethambutol (E)
- **Fixed-dose combinations (FDCs)** are preferred:
  - Advantages: fewer tablets, reduced prescription errors, better adherence, prevents selective drug intake.
  - Examples: RH, RHZ, RHZE.

### 2.3.2 TB Treatment Regimens
- Regimens include initial (intensive) and continuation phases.
- Written as: [Initial phase]/[Continuation phase] (e.g., 2RHZE/4RH).
- Duration in months precedes drug abbreviations.

### 2.3.3 Recommended Treatment Regimen Based on Disease Classification
- **Drug-susceptible TB (new and previously treated)**:
  - Standard: **2RHZE/4RH**
  - For TB meningitis, bone/joint TB: **2RHZE/10RH** (steroids may be added for meningitis).
- **Rifampicin-resistant TB (RR/MDR-TB)**:
  - Short-course regimen: 9–11 months (for new MDR patients without FQ/injectable resistance).
  - Standard regimen: 20–24 months (for previously treated MDR patients).

### 2.3.4 Recommended Standard Regimens in Uganda

#### I. Drug-Susceptible TB
- **Initial phase (2 months)**: RHZE
  - Rapidly kills bacilli; renders patients non-infectious within ~2 weeks.
- **Continuation phase (4 months)**: RH
  - Eliminates residual bacilli and prevents relapse.

##### Adult Dosing (≥15 years, by weight)
- **33–39 kg**: 2 tablets of RHZE (150/75/400/275 mg) and RH (150/75 mg)
- **40–54 kg**: 3 tablets
- **55–70 kg**: 4 tablets
- **>70 kg**: 5 tablets

#### II. Rifampicin-Resistant TB
- Treated with second-line regimens per national RR/MDR-TB guidelines.

### 2.3.5 Adjunctive Therapy
- **Pyridoxine (Vitamin B6)**:
  - Given to all patients on isoniazid (25 mg daily).
  - Prevents peripheral neuropathy.
  - Higher dose (up to 200 mg) if neuropathy occurs.
- **Prednisolone**:
  - Used in TB meningitis or severe inflammatory complications.
  - Dose: 1–2 mg/kg/day (max 60 mg) for 4 weeks, then taper over 2 weeks.

### 2.3.6 Managing Common Side Effects of Anti-TB Drugs
- **Nausea, abdominal pain (Z, R)**: Give with small meal or at bedtime.
- **Joint pains (Z)**: Use analgesics (ibuprofen, paracetamol).
- **Burning feet (H)**: Pyridoxine 25–100 mg daily.
- **Orange/red urine (R)**: Reassure patient; harmless.
- **Skin rash (any drug)**: Stop all drugs; reintroduce one at a time or refer.
- **Deafness, vertigo (S)**: Stop streptomycin; use ethambutol.
- **Jaundice (H, R, Z)**: Stop all drugs until resolved; restart cautiously.
- **Mental confusion (H, R, Z)**:
  - If jaundiced: treat as liver failure.
  - If not: increase pyridoxine.
- **Visual impairment (E)**: Stop ethambutol; refer.

### 2.3.7 Treatment Monitoring
- **Laboratory monitoring (pulmonary TB)**:
  - Sputum smear at end of initial phase (2 months), 5 months, and 6 months.
  - Positive smear at 2 months: do Xpert MTB/RIF.
    - If RR: refer for MDR treatment.
    - If RS: continue first-line; explore adherence; repeat smear at 3 months.
  - Positive smear at 5 or 6 months: diagnose treatment failure; do Xpert.
- **Clinical monitoring**:
  - Essential for children and EPTB.
  - Assess weight gain, symptom reduction.
- **Radiological monitoring**:
  - Not used alone; must accompany sputum/clinical monitoring.

### 2.3.8 Defining Treatment Outcomes (Drug-Susceptible TB)
- **Cured**: Smear/culture-negative at end of treatment and on at least one prior occasion.
- **Treatment completed**: Completed treatment without failure, but no bacteriological confirmation of cure.
- **Treatment failed**: Smear/culture-positive at month 5 or later, or smear-positive at 2 months after starting negative.
- **Died**: Death before or during treatment (any cause).
- **Lost to follow-up**: Treatment interrupted for ≥2 consecutive months.
- **Not evaluated**: Outcome unknown (e.g., transferred out).
- **Treatment success**: Cured + treatment completed.

### 2.3.9 Treatment Adherence
- **Directly Observed Therapy (DOT)** is key:
  - **Facility-based DOT**: Observed by health worker (for inpatients or those near facility).
  - **Community-based DOT (CB-DOT)**: Observed by trained community member (VHT, family, etc.).
- **Implementation in rural settings**:
  - Sub-county Health Worker (SCHW) coordinates.
  - VHT/LC1 identifies treatment supporter.
  - SCHW trains supporter, provides 2-week drug supply, and supervises.
- **Implementation in urban settings**:
  - Use Community Linkage Facilitators (CLFs).
  - Provide 2-week (intensive) or 4-week (continuation) drug supply.
  - Strengthen referral systems and integrate TB/HIV services.
- **Private providers**:
  - Train on TB diagnosis, recording, and reporting.
  - Provide free anti-TB drugs; monitor for adherence to NTLP guidelines.

## 2.4 Preventive Tuberculosis Therapy

### 2.4.1 Why TB Preventive Therapy
- Prevents progression from latent TB infection (LTBI) to active disease.
- Reduces TB risk by >60%; up to 83% with 12-month isoniazid.
- Recommended for high-risk groups.

### 2.4.2 Target Populations
- People living with HIV/AIDS (PLHIV)
- Child contacts (<5 years) of infectious TB patients
- Persons with immunosuppression (e.g., diabetes)
- PLHIV in congregate settings (prisons, IDPs, health workers)

### 2.4.3 Principles of Initiation
1. Diagnose LTBI (e.g., TST ≥5 mm in HIV+ or ≥10 mm in HIV–).
2. Exclude active TB using symptom screening.
3. Use effective regimens (e.g., isoniazid monotherapy or with rifampicin).

### 2.4.4 Isoniazid Preventive Therapy (IPT)
- **For PLHIV**:
  - Screen with 4-symptom tool (current cough, fever, weight loss, night sweats).
  - If no symptoms: offer 6 months IPT (10 mg/kg/day), regardless of CD4, ART status, or pregnancy.
  - TST not required but preferred if feasible.
- **For children**:
  - HIV+ children >12 months: 6 months IPT if no active TB.
  - HIV+ infants <12 months: IPT only if TB contact and no active TB.
  - All children <5 years with TB contact: 6 months IPT after excluding active TB.

### 2.4.5 IPT in Special Situations
- **Pregnancy**: Safe; do not exclude pregnant women from IPT.
- **MDR-TB contacts**: IPT not recommended; use clinical monitoring and infection control.
- **Injecting drug users**: Screen for TB, HIV, hepatitis; provide harm reduction.

### 2.4.6 Monitoring for Toxicity
- Watch for hepatotoxicity (anorexia, nausea, jaundice, dark urine).
- Baseline and periodic LFTs recommended for:
  - History of liver disease
  - Alcohol use
  - HIV infection
  - Age >35 years
  - Pregnancy/postpartum

### 2.4.7 Facilitating Adherence
- Monthly follow-up; initial check at 2 weeks.
- Address side effects, provide education, reduce stigma.
- If active TB develops during IPT: stop IPT and start full TB treatment.

## 2.5 Treatment of Tuberculosis in Special Situations

### 2.5.1 Pregnancy
- Screen and test as in non-pregnant women; avoid CXR if possible.
- Standard regimen **2RHZE/4RH** is safe.
- Avoid aminoglycosides (ototoxic to fetus) and ethionamide (teratogenic) in DR-TB.
- Screen for HIV; manage per national guidelines.

### 2.5.2 Breastfeeding
- Treat with standard regimen.
- Anti-TB drugs in breast milk are insufficient for infant treatment/prophylaxis.
- Investigate infant for TB:
  - If TB disease: full treatment.
  - If no TB: 6 months IPT (10 mg/kg).
- Continue breastfeeding with infection control measures.
- Delay BCG vaccination until after IPT completion.

### 2.5.3 Liver Disease
- In severe liver disease: consider regimens without rifampicin (e.g., streptomycin + ethambutol).
- Refer to higher-level facility.

### 2.5.4 Drug-Induced Liver Injury (DILI)
- Suspect if jaundice ± abdominal pain, nausea, vomiting.
- If ALT/AST >3x upper limit: stop all drugs until normal.
- Reintroduce drugs cautiously, avoiding most hepatotoxic agents (Z, H) first.

### 2.5.5 Renal Failure
- Isoniazid, rifampicin, pyrazinamide: normal doses (hepatic elimination).
- Give pyridoxine to prevent neuropathy.
- Refer to higher-level care.

### 2.5.6 Contraceptives
- Rifampicin reduces efficacy of estrogen-containing contraceptives.
- Use high-estrogen pills (e.g., NewFem, Ovral) or add barrier methods.

### 2.5.7 Bone, Joint, and Spinal TB
- Treat with **2RHZE/10RH** (9–12 months total).
- Surgery considered for:
  - Poor response to chemotherapy
  - Cord compression with neurological deficits
  - Spinal instability

### 2.5.8 TB Meningitis
- Treat with **2RHZE/10RH** (9–12 months).
- Use ethambutol (adults) or aminoglycoside (children).
- Add adjunctive corticosteroids (dexamethasone or prednisolone tapered over 6–8 weeks).

## 2.6 Drug-Resistant Tuberculosis

### 2.6.1 Magnitude
- MDR-TB prevalence (2010 survey):
  - New TB patients: 1.4%
  - Previously treated: 12.1% rifampicin resistance, 21.1% isoniazid resistance.

### 2.6.2 Definition
- **Mono-resistance**: One first-line drug.
- **Poly-resistance**: >1 first-line drug (not H+R).
- **MDR-TB**: Resistant to at least H and R.
- **Pre-XDR-TB**: MDR plus resistance to FQ or injectable (not both).
- **XDR-TB**: MDR plus resistance to FQ and injectable.

### 2.6.3 Risk Factors
- Inadequate treatment due to:
  - **Health system**: Poor DOT, wrong regimens, lack of monitoring.
  - **Drug factors**: Stock-outs, poor quality, improper storage.
  - **Patient factors**: Poor adherence, alcohol/substance abuse, malabsorption, comorbidities (e.g., diabetes).

### 2.6.4 Diagnosis
- Suspect DR-TB in:
  - Contacts of DR-TB
  - Relapse, failure, or loss to follow-up
  - Smear-positive at 2–3 months on first-line treatment
  - HIV-positive presumptive TB
  - HCWs, prisoners
- Test with Xpert MTB/RIF or LPA.
- Confirm with culture and DST.

### 2.6.5 Treatment
- Initiated by DR-TB Expert Review Panels.
- **Shorter regimen (9–12 months)**: For new RR/MDR-TB without FQ/injectable resistance.
- **Standard regimen (20–24 months)**: For complex cases.
- **Phases**:
  - Intensive: ≥6 months (injectable + 4 oral drugs)
  - Continuation: 12–14 months (4 oral drugs)

### 2.6.6 Anti-TB Drug Groups (for DR-TB)
- **Group A (FQs)**: Levofloxacin, moxifloxacin (core drugs).
- **Group B (Injectables)**: Amikacin, capreomycin, kanamycin.
- **Group C (Other core)**: Ethionamide, cycloserine, linezolid, clofazimine.
- **Group D1 (Add-ons)**: Pyrazinamide, ethambutol, high-dose isoniazid.
- **Group D2**: Bedaquiline, delamanid (new drugs).
- **Group D3**: Carbapenems, PAS (last resort).

### 2.6.7 Building an MDR-TB Regimen
- Minimum 5 effective drugs.
- Stepwise approach:
  1. Choose injectable (Group B).
  2. Add FQ (Group A).
  3. Add ≥2 Group C drugs.
  4. Add Group D1 drugs (Z, E).
  5. Add Group D2/D3 if needed.

### 2.6.8 Monitoring MDR-TB Treatment
- **Clinical**: Symptom improvement, weight gain (children).
- **Bacteriological**: Monthly smear and culture until conversion (2 consecutive negatives ≥30 days apart).
- **Radiological**: CXR every 6 months or if clinically indicated.

## 2.7 Tuberculosis in Children

### 2.7.1 Introduction
- Children account for ~7.5% of TB cases in Uganda (underreported; estimated 15–20%).
- Higher risk of infection, disease, and severe forms (e.g., TB meningitis) due to immature immunity.
- Mainly primary TB; older children may have reactivation disease.

### 2.7.2 Risk Factors
- **Infection**: Close/prolonged contact with infectious TB case; high community prevalence.
- **Disease**: Age <5 years (especially <2), HIV, severe malnutrition, measles/pertussis, immunosuppression.
- **Severe disease**: Age <1 year, no BCG vaccination.

### 2.7.3 Presentation (Presumptive TB if any of the following)
- Persistent cough ≥2 weeks
- Prolonged fever ≥2 weeks
- Poor weight gain ≥1 month (weight loss, MUAC in red zone, flattening growth curve)
- Household contact with PTB
- Reduced playfulness/poor feeding with above symptoms

### 2.7.4 Diagnosis
- Seek bacteriological confirmation (Xpert preferred).
- **Tuberculin Skin Test (TST)**:
  - Positive if ≥5 mm in HIV+, malnourished, or immunosuppressed children.
  - Positive if ≥10 mm in other children.

### 2.7.5 Treatment
- **New TB (excluding meningitis/bone)**: **2RHZE/4RH**
- **TB meningitis or bone TB**: **2RHZE/10RH**
- **Dosing (by weight)**:
  - H: 10 mg/kg (7–15)
  - R: 15 mg/kg (10–20)
  - Z: 35 mg/kg (30–40)
  - E: 20 mg/kg (15–25)
- Streptomycin not recommended in children.
- Use FDCs by weight band (4–7 kg: 1 tablet; 8–11 kg: 2; 12–15 kg: 3; 16–24 kg: 4; ≥25 kg: adult doses).

### 2.7.6 Adjunct Therapy
- **Pyridoxine**: 12.5–25 mg/day for HIV+ or malnourished children.
- **Prednisolone**: 2 mg/kg/day for 4 weeks (TB meningitis or airway obstruction), then taper.

### 2.7.7 Follow-Up
- Every 2 weeks in first month, then monthly.
- Weigh at each visit; adjust dose.
- Monitor for adherence, hepatitis, and opportunistic infections (if HIV+).
- CXR not needed if responding well.

### 2.7.8 Prevention
- **BCG**: Given at birth; protects against severe TB (not in confirmed HIV+ infants).
- **IPT**: 6 months for:
  - All children <5 years with TB contact
  - All HIV+ children (after excluding active TB)
- **Contact screening**: Prioritize contacts of bacteriologically confirmed PTB, MDR-TB, PLHIV, and children <5 years.

### 2.7.9 TB/HIV Co-infection in Children
- Start TB treatment immediately.
- Start ART within 2–8 weeks of TB treatment start.
- **ART regimens**:
  - **<3 years**: AZT+3TC+ABC (preferred); ABC+3TC+NVP (alternative)
  - **≥3 years**: ABC+3TC+EFV or TDF+3TC+EFV
- If already on ART:
  - Substitute NVP with EFV if on NVP-based regimen.
  - Continue if on EFV or triple NRTI.

### 2.7.10 TB Immune Reconstitution Inflammatory Syndrome (IRIS)
- Worsening TB symptoms within 3 months of ART start.
- Risk factors: low CD4, extensive TB, early ART.
- **Management**:
  - Continue TB and ART.
  - Give prednisolone 1–2 mg/kg/day for 1–2 weeks, then taper.
  - Rule out treatment failure or other infections.

## 2.8 TB/HIV Co-infection

### 2.8.1 Introduction
- HIV is the strongest risk factor for TB (20–37x higher risk).
- TB causes ~27% of HIV-related adult deaths, ~30% in children.
- In Uganda, ~45% of TB patients are HIV+.

### 2.8.2 TB Prevention in HIV
- **Intensified Case Finding (ICF)**: Screen all PLHIV at every visit using 4-symptom tool.
- **IPT**: Offer to all PLHIV after excluding active TB.
- **Infection Control**: Implement in all health facilities and congregate settings.

### 2.8.3 HIV Care in TB Clinics
- **Provider-Initiated Testing and Counselling (PITC)**: Offer to all presumptive/diagnosed TB patients.
- **Co-trimoxazole Preventive Therapy (CPT)**: Give to all HIV+ TB patients, regardless of CD4.
- **ART**: Start in all HIV+ TB patients; begin within 8 weeks of TB treatment.

### 2.8.4 Community Involvement
- Engage VHTs, support groups, and CBOs in:
  - Case finding
  - Treatment support (DOT, ART adherence)
  - Reducing stigma

### 2.8.5 Presentation of TB in HIV
- **Early HIV**: Similar to HIV– (cavitation, smear-positive).
- **Late HIV**: Atypical (infiltrates without cavitation, smear-negative, extra-pulmonary, disseminated).

### 2.8.6 Diagnosis in HIV
- Use Xpert MTB/RIF as initial test.
- Consider urine LAM in seriously ill or CD4 ≤100.
- CXR often atypical; clinical judgment critical.

### 2.8.7 TB Treatment in HIV
- Same regimens as HIV– patients.
- Ensure DOT and adherence support.
- Start ART within 8 weeks of TB treatment.

### 2.8.8 TB-ART Co-treatment Regimens
- **Adults**: TDF+3TC+EFV or AZT+3TC+EFV
- **Children <3 years**: AZT+3TC+ABC
- **Children ≥3 years**: ABC+3TC+EFV
- **Note**: Avoid NVP with rifampicin (use EFV instead).

### 2.8.9 Immune Reconstitution Syndrome (IRIS)
- Paradoxical worsening after ART start.
- **Management**: Continue TB/ART; prednisolone 1 mg/kg/day for 2 weeks, then taper.

## 2.9 Tuberculosis Infection Control (TB IC)

### 2.9.1 Introduction
- TB spreads via airborne droplet nuclei (<5 µm).
- Most infectious: untreated smear-positive pulmonary or laryngeal TB.

### 2.9.2 TB IC Measures (Hierarchy)
1. **Administrative controls** (highest priority):
   - Prompt identification, isolation, and treatment of presumptive TB.
   - Cough hygiene education.
   - Fast-track TB suspects in clinics.
2. **Environmental controls**:
   - Natural ventilation (open windows/doors).
   - Bed spacing ≥2.5 m (head-to-foot arrangement).
   - Avoid overcrowding.
3. **Personal protection**:
   - N95 respirators for HCWs in DR-TB settings.
   - Surgical masks for infectious patients.

### 2.9.3 In Households
- Ensure early diagnosis and treatment adherence.
- Patient should:
  - Sleep alone in well-ventilated room.
  - Spend time outdoors.
  - Practice cough etiquette.
- Screen household contacts for TB and HIV.
- HIV+ or child contacts of MDR-TB: minimize exposure; regular follow-up.

## 2.10 Tuberculosis Laboratory Services

### 2.10.1 Diagnostic Methods
- **Microscopy**: Widely available; low sensitivity in HIV+.
- **Xpert MTB/RIF**: First test for all presumptive TB.
- **Culture**: Gold standard for sensitivity and DST.
- **Histopathology**: For EPTB.

### 2.10.2 Network in Uganda
- **Microscopy**: ~1,336 diagnostic TB units (DTUs).
- **Xpert**: 111 machines in 105 sites (public, PNFP, private).
- **Culture/DST**: 9 functional labs (NTRL is Supra-national Reference Lab).
- **Sample transport**: 100 hub network with motorcycle riders.

### 2.10.3 External Quality Assurance (EQA)
- Required for all labs (microscopy, culture, molecular).
- Includes blinded rechecking of slides.

## 2.11 TB Monitoring and Evaluation

### 2.11.1 Key Indicators

#### Case Finding
- TB case detection rate
- Proportion of childhood TB cases

#### Case Holding
- Cure rate
- Treatment completion rate
- Treatment success rate
- Lost to follow-up rate
- Death rate
- Treatment failure rate

#### TB/HIV Collaborative Activities
- Proportion of TB patients tested for HIV
- Proportion of HIV+ TB patients on CPT and ART
- Proportion of eligible PLHIV on IPT

#### Drug-Resistant TB
- % of DR-TB contacts screened
- Number of DR-TB cases started on treatment
- DR-TB treatment success rate

#### Laboratory Services
- % of smear-positive PTB registered for treatment
- % of MDR-TB identified from cultures

### 2.11.2 Data Reporting
- **Facility → District → National**
- Use standardized TB registers and quarterly report forms.
- Report through HMIS and NTLP-specific tools.

# National Tuberculosis and Leprosy Programme (NTLP) Manual — 3rd Edition  
**Source**: Ministry of Health, Republic of Uganda — *Manual for Management and Control of Tuberculosis and Leprosy in Uganda, 3rd Edition (March 2017)*  
**Source URL**: https://health.go.ug/sites/default/files/NTLP%20Manual%203rd%20edition_17th%20Aug_final.pdf  

---

## SECTION 1: INTRODUCTION AND DESCRIPTION OF THE NTLP

### 1.1 Introduction

#### 1.1.1 Geography and Demography  
Uganda is a landlocked country in East Africa, bordered by South Sudan (north), Kenya (east), Tanzania and Rwanda (south), and the Democratic Republic of Congo (west). It covers a surface area of **241,038 km²**. The capital is Kampala, and English is the official language. Uganda has a tropical climate with two rainy and two dry seasons.

According to the 2014 national census, Uganda’s population was **34.9 million**, with **50% under 15 years** of age. Approximately **82% live in rural areas**. Life expectancy at birth is **63.3 years** (62.2 for men, 64.2 for women). Infant and under-five mortality rates are **53 and 80 per 1,000 live births**, respectively. Maternal mortality declined from **438 to 360 per 100,000 live births** between 2011 and 2013.

#### 1.1.2 Health Service Delivery  
Health services are delivered through public and private sectors, each covering about 50% of the population. The **public sector** includes Central and Local Governments. The **private sector** comprises Faith-based and NGO private not-for-profit (PNFP) organizations, for-profit providers, and traditional medicine practitioners. The **Ministry of Health (MoH)** leads policy, resource mobilization, and technical guidance.

#### 1.1.3 Burden of Tuberculosis  
The 2015 National TB Prevalence Survey reported:
- **TB prevalence**: 253/100,000 population  
- **TB incidence**: 234/100,000 population  
- **HIV co-infection**: 24% of TB patients  
- **TB mortality** (excluding HIV): 12/100,000 (2014)  
- **Estimated MDR-TB cases**: >1,040 annually  
- **Actual MDR-TB case finding**: ~200/year  

These figures highlight a significant gap between estimated and notified cases, underscoring the need for intensified case finding.

#### 1.1.4 Burden of Leprosy  
Uganda achieved **national elimination of leprosy as a public health problem in 2004**, sustained through 2015. However:
- **New case detection rate** declined from 1.12 (2008) to **0.7/100,000** (2015)  
- **25% of new cases** had Grade 2 disabilities at diagnosis  
- **5% of new cases** were children (<15 years)  
- An estimated **2,000 persons** live with leprosy-related rehabilitation needs  
- **Leprosy “hot spots”** persist in some districts despite overall low endemicity  

All districts must maintain active surveillance.

---

### 1.2 The National Tuberculosis and Leprosy Program (NTLP)

The NTLP is a disease control program under the **Department of National Disease Control**, MoH. Its core functions are:
1. Establish nationwide facilities for quality TB and leprosy diagnosis and treatment  
2. Coordinate and supervise prevention and care implementation  
3. Prevent and manage leprosy-related disabilities  

The NTLP aligns with the **WHO End TB Strategy (2014)** and the **Global Leprosy Strategy 2016–2020**.

#### Pillars of the End TB Strategy:
1. **Integrated, patient-centred care and prevention**  
   - Early diagnosis with universal DST  
   - Treatment for all, including DR-TB  
   - TB/HIV collaboration  
   - Preventive therapy and vaccination  
2. **Bold policies and supportive systems**  
   - Political commitment, UHC, social protection  
3. **Intensified research and innovation**

#### Global Leprosy Strategy Pillars:
1. Strengthen government ownership  
2. Stop leprosy and complications  
3. Stop discrimination and promote inclusion  

---

### 1.2.1 Organisation Structure of the NTLP

The NTLP is structured for national leadership and cascade support down to communities. Key roles by level (chatbot-friendly bullets):

- National (Central Unit — Program Manager + NTRL)
  - Formulate and revise policies and guidelines
  - Develop strategic and operational plans
  - Mobilize resources and set standards
  - Ensure quality assurance, training and M&E
  - Conduct surveillance of drug-resistant TB and operational research

- Regional (RTLP — Regional TB & Leprosy Focal Person)
  - Support and supervise districts
  - Mentor District TB and Leprosy Supervisors (DTLS)
  - Disseminate policies and guidelines and conduct regional training
  - Lead regional M&E and operational research

- District (District Health Officer + DTLS)
  - Plan and prioritise TB/leprosy interventions
  - Supervise HSD in-charges and health workers
  - Ensure drug availability at facilities and validate TB data
  - Monitor and evaluate district-level TB activities

- Health Sub-District (HSD)
  - Implement TB and leprosy services at sub-district facilities
  - Coordinate with community structures and HSD focal persons

- Community (VHTs, Local Council III)
  - Identify and refer presumptive TB cases
  - Provide treatment support (DOT) and community follow-up

*(See Table 1.1 in original manual for the full responsibilities matrix.)*

---

## SECTION 2: TUBERCULOSIS

### 2.1 Tuberculosis Disease

#### 2.1.1 Causative Organism  
TB is caused by *Mycobacterium tuberculosis* complex:
- *M. tuberculosis* (most common)
- *M. bovis*, *M. africanum*, *M. microti*  

Collectively called **tubercle bacilli** or **acid-fast bacilli (AFB)** due to staining properties.

#### 2.1.2 Transmission  
Occurs via **airborne droplet nuclei** (<5 µm) expelled when infectious pulmonary TB patients **cough, sneeze, or sing**. Transmission is enhanced by:
- Poor ventilation  
- Prolonged close contact  
- High bacillary load (smear-positive)  
- High community TB prevalence  

Risk is low with occasional contact or extra-pulmonary TB.

#### 2.1.3 Infection and Development of TB Disease  
- **Primary infection**: Bacilli multiply in lungs/lymph nodes; immunity develops in 6–8 weeks in ~90% of people → **latent TB infection (LTBI)**.  
- **Primary TB disease**: ~10% develop active disease soon after infection (e.g., in HIV, malnutrition).  
- **Post-primary (reactivation) TB**: Dormant bacilli reactivate later due to waning immunity; accounts for ~90% of cases.  

*(See Figure 2.1: Infection and Development of TB Disease)*

---

### 2.2 Diagnosis of Tuberculosis

#### Key Principles:
- Follow the **NTLP diagnostic algorithm**  
- Offer **HIV testing** to all presumptive TB patients  
- Screen for **drug resistance** in high-risk groups  
- **Record and notify** all diagnosed cases, regardless of treatment start  

#### 2.2.1 Approach to Diagnosis  
Use the **Intensified TB Case Finding (ICF) tool** at all entry points. Presumptive TB if:
- **Constitutional symptoms**: evening fever, weight loss, night sweats, anorexia  
- **Pulmonary TB (PTB)**: cough >2 weeks, chest pain, hemoptysis, dyspnea  
- **In HIV/immunosuppressed**: *any duration* of respiratory symptoms is suggestive  

#### 2.2.2 Laboratory Diagnosis  

**Microscopy**  
- Ziehl-Neelsen or fluorescence microscopy  
- Requires **2 specimens**: 1 spot + 1 early morning  
- Low sensitivity in HIV+ and children  

**Xpert MTB/RIF (GeneXpert)**  
- **First test** for all presumptive TB  
- Detects *M. tuberculosis* and **rifampicin resistance** (rpoB mutation)  
- Validated for sputum, lymph node, CSF, pleural fluid, gastric aspirates  

**Xpert MTB/RIF — common results and interpretation**

- MTB detected
  - Bacteriologically confirmed TB. Start TB treatment and follow NTLP guidance for management.

- MTB not detected
  - Does not exclude TB, especially in children, HIV-positive patients, or EPTB. Further evaluation required (clinical assessment, CXR, other tests).

- Rifampicin resistance detected
  - Indicates rifampicin-resistant TB (RR-TB). Refer for full phenotypic and/or molecular DST and manage per RR/MDR-TB guidelines.

- Rifampicin susceptible
  - Treat as rifampicin-susceptible (drug-sensitive) TB. Note this does not exclude resistance to other first-line drugs (H, Z, E).

**Line Probe Assay (LPA)**  
- Detects resistance to **rifampicin and isoniazid**  
- Used for rapid MDR confirmation  

**Culture**  
- Gold standard (solid LJ or liquid MGIT)  
- Takes **6–8 weeks**; enables DST  
- Recommended for:  
  - Smear-negative HIV+ suspects  
  - Treatment failure  
  - Previously treated patients  

**TB LAM (Urine Antigen Test)**  
- For **HIV+ inpatients** with CD4 ≤100 or "seriously ill" (RR >30/min, Temp >39°C, HR >120/min, unable to walk unaided)  

#### 2.2.3 Radiology  
**CXR findings consistent with TB**:  
- Cavitation  
- Miliary pattern  
- Pleural effusion  
- Mediastinal lymphadenopathy  

All bacteriologically negative presumptive TB patients should have CXR. If suggestive, **start treatment**.

#### 2.2.4 Histology  
Used for EPTB (e.g., lymphadenitis). Granulomatous inflammation confirms diagnosis. Samples via:
- Fine needle aspiration (lymph nodes)  
- Tissue biopsy (pleura, pericardium, skin, liver)  

#### 2.2.5 Standard TB Case Definitions  

**Standard TB case definitions (chatbot-ready)**

- Presumptive TB patient: any patient presenting with symptoms or signs suggestive of TB (screen positive on ICF).

- Bacteriologically confirmed TB patient: a patient with a biological specimen positive by smear microscopy, culture, or a WHO-recommended NAAT (e.g., Xpert).

- Clinically diagnosed TB patient: a patient not bacteriologically confirmed but started on full TB treatment based on clinical judgement, CXR, or histology. Reclassify to confirmed if later bacteriologically positive.

*Note: Reclassify as "confirmed" if later bacteriologically positive.*

#### 2.2.6 Classification of TB Patients  

**1. Site of Disease**  
- **Pulmonary TB (PTB)**: Lung parenchyma or tracheobronchial tree  
- **Extra-pulmonary TB (EPTB)**: Other organs (pleura, lymph nodes, meninges, etc.)  
- *Patients with both are classified as PTB*

**2. Treatment History**  
- **New**: Never treated or <1 month  
- **Previously treated**:  
  - Relapse  
  - Treatment after failure  
  - Treatment after loss to follow-up (≥2 months interruption)  
  - Other (unknown outcome)  

**3. HIV Status**  
- HIV-positive, HIV-negative, or unknown  

**4. Drug Resistance**  
- **Mono-resistance**: One first-line drug  
- **Poly-resistance**: >1 first-line drug (not H+R)  
- **MDR-TB**: Resistant to **isoniazid + rifampicin**  
- **XDR-TB**: MDR + resistance to **any fluoroquinolone + any injectable** (amikacin, capreomycin, kanamycin)  
- **RR-TB**: Rifampicin resistance (by Xpert or DST); includes MDR/XDR  

#### 2.2.7 Post-TB Patients  
Patients cured of TB who present later with respiratory symptoms (cough, dyspnea, hemoptysis).  
- **First**: Repeat standard TB evaluation (sputum, CXR)  
- **If TB+**: Treat as retreatment  
- **If TB–**: Evaluate for **post-TB lung disease** (bronchiectasis, COPD, aspergillosis)  
- **Avoid repeated empirical TB treatment** without confirmation  

---

### 2.3 Treatment of Tuberculosis

#### Aims:
- Cure the patient  
- Prevent death/complications  
- Prevent relapse & transmission  
- Prevent drug resistance  

#### 2.3.1 Anti-TB Medicines  
**First-line drugs** (for drug-susceptible TB):  
- Rifampicin (R)  
- Isoniazid (H)  
- Pyrazinamide (Z)  
- Ethambutol (E)  

**Fixed-Dose Combinations (FDCs)** are preferred (e.g., RH, RHZ, RHZE) to:
- Reduce prescription errors  
- Improve adherence  
- Prevent selective drug intake  

#### 2.3.2 TB Treatment Regimens  
Written as: **[Initial phase]/[Continuation phase]**  
Example: **2RHZE/4RH** = 2 months RHZE + 4 months RH  

#### 2.3.3 Recommended Regimens by Classification  

**Recommended regimens (concise)**

- Drug-susceptible TB (new or previously treated, if rifampicin resistance excluded)
  - Standard regimen: 2RHZE (2 months) followed by 4RH (4 months) — written 2RHZE/4RH.

- TB meningitis or bone/joint TB
  - Extended regimen: 2RHZE followed by 10RH (total often 9–12 months). Add adjunctive steroids for TB meningitis.

- Rifampicin-resistant / MDR-TB
  - Short-course regimen (9–11 months): for selected new RR/MDR patients without FQ/injectable resistance.
  - Standard (conventional) regimen (20–24 months): for previously treated or complex MDR/XDR cases; individualized as needed.

#### 2.3.4 Standard Regimens in Uganda  

**I. Drug-Susceptible TB**  
- **Initial phase (2 months)**: RHZE → rapid bacillary kill, non-infectious by ~2 weeks  
- **Continuation phase (4 months)**: RH → eliminate residual bacilli  

**Adult Dosing (≥15 years)**  
**Adult Dosing (≥15 years)**

- 33–39 kg: 2 tablets of RHZE in the intensive phase (FDC 150/75/400/275) and 2 tablets of RH in the continuation phase (150/75).
- 40–54 kg: 3 tablets (intensive and continuation phases as per FDC/NTLP guidance).
- 55–70 kg: 4 tablets.
- >70 kg: 5 tablets.

(Follow national FDC weight bands and product inserts for exact tablet composition and strengths.)

**II. Rifampicin-Resistant TB**  
Treat per national **RR/MDR-TB guidelines** with second-line regimens.

#### 2.3.5 Adjunctive Therapy  
- **Pyridoxine (Vitamin B6)**: 25 mg/day with isoniazid to prevent neuropathy  
- **Prednisolone**: 1–2 mg/kg/day (max 60 mg) for 4 weeks + 2-week taper (for TB meningitis, severe inflammation)  

#### 2.3.6 Managing Common Side Effects  

**Common side-effects and management (chatbot-friendly)**

- Nausea / abdominal pain — often Pyrazinamide (Z) or Rifampicin (R)
  - Give drugs with a small meal or at bedtime; symptomatic relief (antiemetics) if needed.

- Joint pains — commonly Pyrazinamide (Z)
  - Use analgesics (paracetamol, ibuprofen).

- Peripheral neuropathy / burning feet — Isoniazid (H)
  - Give pyridoxine (Vitamin B6) 25–100 mg daily; higher doses if neuropathy occurs.

- Orange/red urine — Rifampicin (R)
  - Reassure patient (harmless discoloration).

- Skin rash — any anti-TB drug
  - Stop all drugs, evaluate; reintroduce one drug at a time when safe or refer to specialist.

- Deafness, vertigo — Streptomycin (S)
  - Stop streptomycin; consider ethambutol as alternative and refer.

- Jaundice / suspected hepatotoxicity — H, R, Z
  - Stop all anti-TB drugs until LFTs normalize; reintroduce cautiously per guidelines.

- Visual impairment — Ethambutol (E)
  - Stop ethambutol and refer for ophthalmologic assessment.

#### 2.3.7 Treatment Monitoring  

**Laboratory (Pulmonary TB)**:  
- Sputum smear at **2, 5, and 6 months**  
- If **positive at 2 months**: Do Xpert → if RR, refer; if RS, continue + adherence counseling  
- If **positive at 5/6 months**: Diagnose **treatment failure**  

**Clinical**: Essential for children/EPTB → assess weight gain, symptom resolution  
**Radiological**: Not standalone; use with sputum/clinical data  

#### 2.3.8 Treatment Outcomes (Drug-Susceptible TB)  

**Treatment outcome categories (clear bullets)**

- Cured: pulmonary TB patient who was bacteriologically positive at start and is smear/culture-negative in the last month of treatment and on at least one prior occasion.

- Treatment completed: completed treatment with no evidence of failure but without bacteriological confirmation of cure.

- Treatment failed: smear/culture positive at month 5 or later, or smear-positive at 2 months after previously negative.

- Died: patient died for any reason before or during treatment.

- Lost to follow-up: treatment interrupted for 2 or more consecutive months or patient did not start treatment.

- Not evaluated: no treatment outcome assigned (including transferred out).

- Treatment success: the sum of cured and treatment completed.

#### 2.3.9 Treatment Adherence  

**Directly Observed Therapy (DOT)** is essential:  
- **Facility-based DOT**: For inpatients or those near facility  
- **Community-based DOT (CB-DOT)**: Observed by VHT, family, or trained community member  

**Rural Implementation**:  
- Sub-county Health Worker (SCHW) coordinates  
- VHT/LC I identifies treatment supporter  
- SCHW trains, supplies drugs (2-weekly), and supervises  

**Urban Implementation**:  
- Use **Community Linkage Facilitators (CLFs)**  
- Provide 2-week (intensive) or 4-week (continuation) drug supply  
- Strengthen TB/HIV integration  

**Private Providers**:  
- Train on diagnosis, recording, reporting  
- Provide free drugs; monitor adherence to NTLP guidelines  

---

### 2.4 Preventive Tuberculosis Therapy

#### 2.4.1 Rationale  
Prevents progression from **latent TB infection (LTBI)** to active disease. Reduces risk by **>60%** (up to 83% with 12-month isoniazid).

#### 2.4.2 Target Populations  
- PLHIV  
- Child contacts (<5 years) of infectious TB  
- Immunosuppressed (e.g., diabetes)  
- PLHIV in congregate settings (prisons, HCWs, IDPs)  

#### 2.4.3 Principles of Initiation  
1. Diagnose LTBI (TST ≥5 mm in HIV+; ≥10 mm in HIV–)  
2. Exclude active TB using symptom screening  
3. Use effective regimens (e.g., isoniazid monotherapy)  

#### 2.4.4 Isoniazid Preventive Therapy (IPT)  
- **PLHIV**: Screen with 4-symptom tool (cough, fever, weight loss, night sweats). If negative, give **6 months IPT (10 mg/kg/day)**, regardless of CD4, ART, or pregnancy.  
- **Children**:  
  - All <5 years with TB contact → 6 months IPT  
  - HIV+ children >12 months → 6 months IPT  
  - HIV+ infants <12 months → IPT only if TB contact  

#### 2.4.5 IPT in Special Situations  
- **Pregnancy**: Safe; continue if started before pregnancy  
- **MDR-TB contacts**: **Do not use IPT**; use clinical monitoring + infection control  
- **Injecting drug users**: Screen for TB/HIV/hepatitis; provide harm reduction  

#### 2.4.6 Monitoring for Toxicity  
Watch for **hepatotoxicity** (anorexia, nausea, jaundice). Baseline/periodic LFTs for:
- Liver disease history  
- Alcohol use  
- HIV infection  
- Age >35 years  
- Pregnancy/postpartum  

#### 2.4.7 Facilitating Adherence  
- Initial follow-up at **2 weeks**, then monthly  
- Address side effects, reduce stigma, educate  
- If active TB develops: **stop IPT**, start full TB treatment  

---

### 2.5 Treatment in Special Situations

#### 2.5.1 Pregnancy  
- Standard regimen **2RHZE/4RH is safe**  
- Avoid **aminoglycosides** (fetal ototoxicity) and **ethionamide** (teratogenic) in DR-TB  
- Screen for HIV; manage per guidelines  

#### 2.5.2 Breastfeeding  
- Treat mother with standard regimen  
- **Infant**:  
  - If TB disease → full treatment  
  - If no TB → **6 months IPT (10 mg/kg)**  
- Continue breastfeeding with infection control  
- **Delay BCG** until after IPT  

#### 2.5.3 Liver Disease  
- In severe disease: consider **streptomycin + ethambutol** (avoid rifampicin)  
- Refer to higher-level facility  

#### 2.5.4 Drug-Induced Liver Injury (DILI)  
- If ALT/AST >3x upper limit: **stop all drugs** until normal  
- Reintroduce cautiously, avoiding Z/H first  

#### 2.5.5 Renal Failure  
- Isoniazid, rifampicin, pyrazinamide: **normal doses** (hepatic elimination)  
- Give **pyridoxine** to prevent neuropathy  

#### 2.5.6 Contraceptives  
- Rifampicin reduces estrogen efficacy → use **high-estrogen pills (NewFem, Ovral)** or add barrier methods  

#### 2.5.7 Bone, Joint, Spinal TB  
- Regimen: **2RHZE/10RH** (9–12 months)  
- Surgery if: poor response, cord compression, spinal instability  

#### 2.5.8 TB Meningitis  
- Regimen: **2RHZE/10RH**  
- Add **adjunctive corticosteroids** (dexamethasone/prednisolone tapered over 6–8 weeks)  

---

### 2.6 Drug-Resistant Tuberculosis

#### 2.6.1 Magnitude  
2010 Drug Resistance Survey:
- **New TB**: 1.4% MDR-TB  
- **Previously treated**: 12.1% rifampicin resistance, 21.1% isoniazid resistance  

#### 2.6.2 Definitions  
- **MDR-TB**: Resistant to **H + R**  
- **XDR-TB**: MDR + resistant to **FQ + injectable**  
- **RR-TB**: Rifampicin resistance (by Xpert/DST)  

#### 2.6.3 Risk Factors  
- Inadequate treatment (wrong regimen, poor adherence, stock-outs)  
- Patient factors (alcohol, diabetes, malabsorption)  

#### 2.6.4 Diagnosis  
Suspect in:
- Contacts of DR-TB  
- Relapse/failure/loss to follow-up  
- Smear-positive at 2–3 months on treatment  
- HIV+ presumptive TB  
- HCWs, prisoners  

Test with **Xpert MTB/RIF** or **LPA**; confirm with **culture + DST**.

#### 2.6.5 Treatment  
- Initiated by **DR-TB Expert Review Panels**  
- **Shorter regimen (9–12 months)**: New RR/MDR-TB without FQ/injectable resistance  
- **Standard regimen (20–24 months)**: Complex cases  

**Phases**:  
- **Intensive**: ≥6 months (injectable + 4 oral drugs)  
- **Continuation**: 12–14 months (4 oral drugs)  

#### 2.6.6 Anti-TB Drug Groups (for DR-TB)  

**Anti-TB drug groups (chatbot-friendly)**

- Group A (Fluoroquinolones): Levofloxacin, moxifloxacin (core drugs)
- Group B (Injectables): Amikacin, capreomycin, kanamycin
- Group C (Other core drugs): Ethionamide, cycloserine, linezolid, clofazimine
- Group D1 (Add-ons): Pyrazinamide, ethambutol, high-dose isoniazid
- Group D2 (New drugs): Bedaquiline, delamanid
- Group D3 (Last resort): Carbapenems, PAS

#### 2.6.7 Building an MDR-TB Regimen  
Minimum **5 effective drugs**:  
1. Choose injectable (Group B)  
2. Add FQ (Group A)  
3. Add ≥2 Group C drugs  
4. Add Group D1 (Z, E)  
5. Add D2/D3 if needed  

#### 2.6.8 Monitoring MDR-TB Treatment  
- **Clinical**: Symptom improvement, weight gain  
- **Bacteriological**: Monthly smear/culture until **conversion** (2 consecutive negatives ≥30 days apart)  
- **Radiological**: CXR every 6 months  

---

### 2.7 Tuberculosis in Children

#### 2.7.1 Introduction  
- Children = **7.5%** of notified TB (underreported; estimated 15–20%)  
- Higher risk of **infection, disease, severe forms** (e.g., TB meningitis) due to immature immunity  
- Mainly **primary TB**; older children may have reactivation  

#### 2.7.2 Risk Factors  
- **Infection**: Close contact with infectious TB, high community prevalence  
- **Disease**: Age <5 years (especially <2), HIV, malnutrition, measles  
- **Severe disease**: Age <1 year, no BCG  

#### 2.7.3 Presentation (Presumptive TB if any):  
- Cough ≥2 weeks  
- Fever ≥2 weeks  
- Poor weight gain ≥1 month  
- Household TB contact  
- Reduced playfulness with above  

#### 2.7.4 Diagnosis  
- **Xpert MTB/RIF** preferred  
- **TST**: ≥5 mm (HIV+/malnourished); ≥10 mm (others)  

#### 2.7.5 Treatment  
#### 2.7.5 Treatment

- New TB (non-severe): 2RHZE/4RH
- TB meningitis or bone TB: 2RHZE/10RH (extended continuation; total often 9–12 months)

**Dosing (by weight)**:  
- H: 10 mg/kg (7–15)  
- R: 15 mg/kg (10–20)  
- Z: 35 mg/kg (30–40)  
- E: 20 mg/kg (15–25)  

**FDCs by weight band**:  
- 4–7 kg: 1 tablet  
- 8–11 kg: 2  
- 12–15 kg: 3  
- 16–24 kg: 4  
- ≥25 kg: adult doses  

*Streptomycin not recommended in children.*

#### 2.7.6 Adjunct Therapy  
- **Pyridoxine**: 12.5–25 mg/day (HIV+/malnourished)  
- **Prednisolone**: 2 mg/kg/day for 4 weeks (meningitis/airway obstruction), then taper  

#### 2.7.7 Follow-Up  
- Every 2 weeks (first month), then monthly  
- Weigh at each visit; adjust dose  
- Monitor for adherence, hepatitis, OIs (if HIV+)  

#### 2.7.8 Prevention  
- **BCG**: At birth (protects against severe TB; **not in confirmed HIV+ infants**)  
- **IPT**: 6 months for:  
  - All <5 years with TB contact  
  - All HIV+ children (after excluding active TB)  
- **Contact screening**: Prioritize contacts of confirmed PTB, MDR-TB, PLHIV, children <5 years  

#### 2.7.9 TB/HIV Co-infection in Children  
- Start TB treatment immediately  
- Start ART within **2–8 weeks** of TB treatment  
- **ART regimens**:  
  - <3 years: AZT+3TC+ABC (preferred)  
  - ≥3 years: ABC+3TC+EFV or TDF+3TC+EFV  
- If on ART: **substitute NVP with EFV**  

#### 2.7.10 TB Immune Reconstitution Inflammatory Syndrome (IRIS)  
- Worsening TB symptoms within **3 months of ART start**  
- **Management**: Continue TB/ART; prednisolone 1–2 mg/kg/day for 1–2 weeks, then taper  

---

### 2.8 TB/HIV Co-infection

#### 2.8.1 Introduction  
- HIV = strongest TB risk factor (**20–37x higher risk**)  
- TB causes **~27% of HIV adult deaths**, **~30% in children**  
- In Uganda, **~45% of TB patients are HIV+**  

#### 2.8.2 TB Prevention in HIV  
- **Intensified Case Finding (ICF)**: Screen all PLHIV at every visit  
- **IPT**: Offer to all PLHIV after excluding active TB  
- **Infection Control**: Implement in all facilities/congregate settings  

#### 2.8.3 HIV Care in TB Clinics  
- **PITC**: Offer HIV testing to all TB patients  
- **CPT**: Give to all HIV+ TB patients (any CD4)  
- **ART**: Start in all HIV+ TB patients within **8 weeks** of TB treatment  

#### 2.8.4 Community Involvement  
Engage VHTs, support groups, CBOs in case finding, treatment support, stigma reduction.

#### 2.8.5 Presentation of TB in HIV  
- **Early HIV**: Similar to HIV– (cavitation, smear+)  
- **Late HIV**: Atypical (infiltrates, smear–, EPTB, disseminated)  

#### 2.8.6 Diagnosis in HIV  
- **Xpert MTB/RIF** = first test  
- **Urine LAM** if CD4 ≤100 or seriously ill  
- CXR often atypical; clinical judgment critical  

#### 2.8.7 TB Treatment in HIV  
- Same regimens as HIV–  
- Ensure DOT and adherence support  
- Start ART within 8 weeks  

#### 2.8.8 TB-ART Co-treatment Regimens  
- **Adults**: TDF+3TC+EFV or AZT+3TC+EFV  
- **Children <3 years**: AZT+3TC+ABC  
- **Children ≥3 years**: ABC+3TC+EFV  
- **Avoid NVP with rifampicin**  

#### 2.8.9 Immune Reconstitution Syndrome (IRIS)  
- Paradoxical worsening after ART start  
- **Management**: Continue TB/ART; prednisolone 1 mg/kg/day for 2 weeks, then taper  

---

### 2.9 Tuberculosis Infection Control (TB IC)

#### 2.9.1 Introduction  
TB spreads via **airborne droplet nuclei** (<5 µm). Most infectious: **untreated smear+ pulmonary/laryngeal TB**.

#### 2.9.2 TB IC Measures (Hierarchy)  

**1. Administrative Controls (Highest Priority)**  
- Prompt identification, isolation, fast-tracking of TB suspects  
- Cough hygiene education (cover mouth, turn away)  
- Designate well-ventilated TB areas in wards/clinics  

**2. Environmental Controls**  
- **Natural ventilation**: Open windows/doors (≥8–12 air changes/hour)  
- **Bed spacing**: ≥2.5 m (head-to-foot arrangement)  
- Avoid overcrowding  

**3. Personal Protection**  
- **N95 respirators** for HCWs in DR-TB settings  
- **Surgical masks** for infectious patients  

#### 2.9.3 In Households  
- Early diagnosis + treatment adherence  
- Patient should:  
  - Sleep alone in well-ventilated room  
  - Spend time outdoors  
  - Practice cough etiquette  
- Screen household contacts for TB/HIV  
- **HIV+ or child contacts of MDR-TB**: minimize exposure; regular follow-up  

---

### 2.10 Tuberculosis Laboratory Services

#### 2.10.1 Diagnostic Methods  
- **Microscopy**: Widely available; low sensitivity in HIV+  
- **Xpert MTB/RIF**: First test for all presumptive TB  
- **Culture**: Gold standard for sensitivity/DST  
- **Histopathology**: For EPTB  

#### 2.10.2 Network in Uganda  
- **Microscopy**: ~1,336 DTUs  
- **Xpert**: 111 machines in 105 sites (public, PNFP, private)  
- **Culture/DST**: 9 labs (NTRL = Supra-national Reference Lab)  
- **Sample transport**: 100 hub network with motorcycle riders  

#### 2.10.3 External Quality Assurance (EQA)  
Required for all labs (microscopy, culture, molecular). Includes blinded rechecking.

---

### 2.11 TB Monitoring and Evaluation

#### 2.11.1 Key Indicators  

**Case Finding**  
- TB case detection rate  
- Proportion of childhood TB cases  

**Case Holding**  
- Cure rate  
- Treatment completion rate  
- Lost to follow-up rate  
- Death/treatment failure rates  

**TB/HIV Collaboration**  
- % TB patients tested for HIV  
- % HIV+ TB patients on CPT/ART  
- % eligible PLHIV on IPT  

**Drug-Resistant TB**  
- % DR-TB contacts screened  
- DR-TB treatment success rate  

**Laboratory Services**  
- % smear+ PTB registered for treatment  
- % MDR-TB identified from cultures  

#### 2.11.2 Data Reporting  
- **Flow**: Facility → District → National  
- **Tools**: Standard TB registers, quarterly reports, HMIS  