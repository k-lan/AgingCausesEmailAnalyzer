I'd like to use ai with the openai api library with gpt-4o-mini to do the following task:

Requirement
Read the text of both files.
    - Data/Email Thread #1.txt
    - Data/Email Thread #2.txt

Analyze the content by email author
    - We'll run this through the ai twice, once for each file (do this in a loop)
    - Output the results to the MD file in a new line for each email and "Brief causes of aging"

Each author lists one or more causes of aging

Create an MD table for information - store in causesofaging.md
- Columns
  - Email Subject Label
  - Author
  - Email Date/time
  - Cause of Aging #
  - Brief Causes of Aging Description - one or two sentences

| Email Subject Label | Author          | Email Date/Time        | Cause of Aging # | Brief Causes of Aging Description                                                                 |
|---------------------|-----------------|------------------------|------------------|-------------------------------------------------------------------------------------------------|
| Re: Project Update  | john.doe@email.com | 2023-10-26 10:00 AM    | 1                | Cellular senescence is a key factor in aging, leading to tissue dysfunction.                     |
| Re: Project Update  | john.doe@email.com | 2023-10-26 10:00 AM    | 2                | Accumulation of DNA damage over time contributes to the aging process.                           |
| Meeting Invitation  | jane.smith@email.com| 2023-10-27 02:30 PM    | 1                | Chronic inflammation accelerates aging by damaging cells and tissues.                             |
| Meeting Invitation  | jane.smith@email.com| 2023-10-27 02:30 PM    | 2                | Telomere shortening limits cell division and contributes to aging.                               |
| FW: Important Info  | peter.pan@email.com | 2023-10-28 09:15 AM    | 1                | Oxidative stress from free radicals damages cellular components, leading to aging.              |
| FW: Important Info  | peter.pan@email.com | 2023-10-28 09:15 AM    | 2                | Glycation, the binding of sugar to proteins, impairs their function and contributes to aging. |