constant_json = {
  "survey_number": "",
  "status": "",
  "survey_assigned_on": "",
  "household_member_count": "",
  "data_collector_signature": "",
  "notes": "",
  "next_section": "",
  "members": "",
  "initial_section": {
    "category_name": "Basic Information",
    "position": 1,
    "page": 1,
    "section": [
      {
        "section_name": "",
        "is_subheader": False,
        "position": 1,
        "qcount": 2,
        "anscount": 0,
        "questions": [
          {
            "title": "Number",
            "qno" : "Number",
            "is_required": True,
            "is_read_only": False,
            "position": 1,
            "others_status": None,
            "qn_ranking": None,
            "answers": [
              {
                "dtype": "box_number",
                "position": 1,
                "placeholder": "Enter the name of the head",
                "options": None,
                "answer_value": "",
                "is_error": False,
                "error_message": "Enter a valid 6 digit number to proceed",
                "keyboard_type": "number",
                "limitation": 6,
                "show_dropdown_modal": None,
                "show_time_picker": None,
                "show_multi_dropdown_modal": None,
                "show_picker": None,
                "ranking": None
              }
            ]
          },
          {
            "title": "Institutional",
            "qno" : "Institutional",
            "is_required": True,
            "is_read_only": False,
            "position": 2,
            "others_status": None,
            "qn_ranking": None,
            "answers": [
              {
                "dtype": "radio",
                "position": 1,
                "placeholder": "Household",
                "options": None,
                "answer_value": True,
                "is_error": False,
                "error_message": "Please select an option to proceed",
                "keyboard_type": None,
                "limitation": None,
                "show_dropdown_modal": None,
                "show_time_picker": None,
                "show_multi_dropdown_modal": None,
                "show_picker": None,
                "ranking": None
              },
              {
                "dtype": "radio",
                "position": 2,
                "placeholder": "Institutional living quarter",
                "options": None,
                "answer_value": False,
                "is_error": False,
                "error_message": "Please select an option to proceed",
                "keyboard_type": None,
                "limitation": None,
                "show_dropdown_modal": None,
                "show_time_picker": None,
                "show_multi_dropdown_modal": None,
                "show_picker": None,
                "ranking": None
              }
            ]
          },
          {
            "title": "Notes",
            "qno" : "Notes",
            "is_required": True,
            "is_read_only": False,
            "position": 3,
            "others_status": None,
            "qn_ranking": None,
            "answers": [
              {
                "dtype": "textarea",
                "position": 1,
                "placeholder": "Household",
                "options": "Lubos kong naunawaan ang layunin ng pananaliksik at Census ng barangay. Nabasa ko at pinaliwanag sa akin ang nilalaman ng kasulatan at kusang loob akong sumasangayon na makibahagi sa proyektong ito. Naunawaan kong magiging kumpidensyal ang lahat ng aking kasagutan. Gayunpaman, pinahihintulutan ko ang paggamit ng akin impormasyon ng barangay kalakip ng paggalang sa aking data privacy rights",
                "answer_value": None,
                "is_error": False,
                "error_message": None,
                "keyboard_type": None,
                "limitation": None,
                "show_dropdown_modal": None,
                "show_time_picker": None,
                "show_multi_dropdown_modal": None,
                "show_picker": None,
                "ranking": None
              }
            ]
          }
        ]
      }
    ]
  },
  "interview_section": [
    {
      "category_name": "A. Identification",
      "position": 2,
      "page": 2,
      "section": [
        {
          "section_name": "",
          "is_subheader": False,
          "position": 2,
          "qcount": 9,
          "anscount": 0,
          "questions": [
            {
              "title": "Province",
              "qno" : "Province",
              "is_required": True,
              "is_read_only": False,
              "position": 1,
              "others_status": None,
              "qn_ranking": 1,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Province Name",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 1
                }
              ]
            },
            {
              "title": "Province ID",
              "qno" : "Province ID",
              "is_required": True,
              "is_read_only": False,
              "position": 2,
              "others_status": None,
              "qn_ranking": 2,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Province ID",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter 2 digit ID to proceed",
                  "keyboard_type": "number",
                  "limitation": 2,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 2
                }
              ]
            },
            {
              "title": "City / Municipality",
              "qno" : "City / Municipality",
              "is_required": True,
              "is_read_only": False,
              "position": 3,
              "others_status": None,
              "qn_ranking": 3,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "City / Municipality",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 3
                }
              ]
            },
            {
              "title": "City / Municipality ID",
              "qno" : "City / Municipality ID",
              "is_required": True,
              "is_read_only": False,
              "position": 4,
              "others_status": None,
              "qn_ranking": 4,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "City / Municipality ID",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter 2 digit ID to proceed",
                  "keyboard_type": "number",
                  "limitation": 2,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 4
                }
              ]
            },
            {
              "title": "Barangay",
              "qno" : "Barangay 1",
              "is_required": True,
              "is_read_only": False,
              "position": 5,
              "others_status": None,
              "qn_ranking": 5,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Barangay name",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 5
                }
              ]
            },
            {
              "title": "Barangay number", 
              "qno" : "Barangay number",
              "is_required": True,
              "is_read_only": False,
              "position": 6,
              "others_status": None,
              "qn_ranking": 6,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Barangay Number",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter 3 digit ID to proceed",
                  "keyboard_type": "number",
                  "limitation": 3,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 6
                }
              ]
            },
            {
              "title": "Name of Respondent",
              "qno" : "Name of Respondent",
              "is_required": True,
              "is_read_only": False,
              "position": 7,
              "others_status": None,
              "qn_ranking": 7,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter name of respondent",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 7
                }
              ]
            },
            {
              "title": "Household Head",
              "qno" : "Household Head",
              "is_required": True,
              "is_read_only": False,
              "position": 8,
              "others_status": None,
              "qn_ranking": 8,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter name of household head",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 8
                }
              ]
            }
          ]
        },
        {
          "section_name": "Address",
          "is_subheader": False,
          "position": 3,
          "qcount": 3,
          "anscount": 0,
          "questions": [
            {
              "title": "Locality",
              "qno" : "Locality",
              "is_required": True,
              "is_read_only": False,
              "position": 1,
              "others_status": None,
              "qn_ranking": 10,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter the locality",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 10
                }
              ]
            },
            {
              "title": "Room / Floor / Unit no and Building name",
              "qno" : "Room / Floor / Unit no and Building name",
              "is_required": True,
              "is_read_only": False,
              "position": 2,
              "others_status": None,
              "qn_ranking": 11,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter room / floor /unit no and building name",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 11
                }
              ]
            },
            {
              "title": "House / Lot and Block no",
              "qno" : "House / Lot and Block no",
              "is_required": True,
              "is_read_only": False,
              "position": 3,
              "others_status": None,
              "qn_ranking": 12,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter the house / lot and block no",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 12
                }
              ]
            },
            {
              "title": "Street Name",
              "qno" : "Street Name",
              "is_required": True,
              "is_read_only": False,
              "position": 4,
              "others_status": None,
              "qn_ranking": 13,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter the street name",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 13
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "category_name": "B. Interview Information",
      "position": 3,
      "page": 3,
      "section": [
        {
          "section_name": "",
          "is_subheader": False,
          "position": 4,
          "qcount": 12,
          "anscount": 0,
          "questions": [
            {
              "title": "Visit",
              "qno" : "Visit",
              "is_required": True,
              "is_read_only": False,
              "position": 1,
              "others_status": None,
              "qn_ranking": 14,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select visit",
                  "options": [
                    "First",
                    "Second"
                  ],
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please select the visit number to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": False,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 14
                }
              ]
            },
            {
              "title": "Date of Visit",  
              "qno" : "Date of Visit",
              "is_required": True,
              "is_read_only": False,
              "position": 2,
              "others_status": None,
              "qn_ranking": 15,
              "answers": [
                {
                  "dtype": "datepicker",
                  "position": 1,
                  "placeholder": "DD/MM/YYYY",
                  "options": None,
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select a date to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": False,
                  "ranking": 15
                }
              ]
            },
            {
              "title": "Time Start",  
              "qno" : "Time Start",
              "is_required": True,
              "is_read_only": False,
              "position": 3,
              "others_status": None,
              "qn_ranking": 16,
              "answers": [
                {
                  "dtype": "timepicker",
                  "position": 1,
                  "placeholder": "",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please select a valid time to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": False,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 16
                }
              ]
            },
            {
              "title": "Time End",
              "qno" : "Time End",
              "is_required": True,
              "is_read_only": True,
              "position": 4,
              "others_status": None,
              "qn_ranking": 17,
              "answers": [
                {
                  "dtype": "timepicker",
                  "position": 1,
                  "placeholder": "",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please select a valid time to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 17
                }
              ]
            },
            {
              "title": "Result",
              "qno" : "Result",
              "is_required": True,
              "is_read_only": True,
              "position": 5,
              "others_status": None,
              "qn_ranking": 18,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select visit",
                  "options": [
                    "Pending",
                    "Callback",
                    "Completed"
                  ],
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please select an option to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 18
                }
              ]
            },
            {
              "title": "Date Next Visit",
              "qno" : "Date Next Visit",
              "is_required": True,
              "is_read_only": True,
              "position": 6,
              "others_status": None,
              "qn_ranking": 19,
              "answers": [
                {
                  "dtype": "datepicker",
                  "position": 1,
                  "placeholder": "",
                  "options": None,
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select a date to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 19
                }
              ]
            },
            {
              "title": "Name of Interviewer",
              "qno" : "Name of Interviewer",
              "is_required": True,
              "is_read_only": False,
              "position": 7,
              "others_status": None,
              "qn_ranking": 20,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 20
                }
              ]
            },
            {
              "title": "Initial",
              "qno" : "Initial 1",
              "is_required": True,
              "is_read_only": False,
              "position": 8,
              "others_status": None,
              "qn_ranking": 21,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter the initial",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 21
                }
              ]
            },
            {
              "title": "Date",
              "qno" : "Date 1",
              "is_required": True,
              "is_read_only": False,
              "position": 8,
              "others_status": None,
              "qn_ranking": 22,
              "answers": [
                {
                  "dtype": "datepicker",
                  "position": 1,
                  "placeholder": "DD/MM/YYYY",
                  "options": None,
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select a date to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": False,
                  "ranking": 22
                }
              ]
            },
            {
              "title": "Name of Supervisor",
              "qno" : "Name of Supervisor 1",
              "is_required": True,
              "is_read_only": False,
              "position": 9,
              "others_status": None,
              "qn_ranking": 23,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 23
                }
              ]
            },
            {
              "title": "Initial",
              "qno" : "Initial 2",
              "is_required": True,
              "is_read_only": False,
              "position": 10,
              "others_status": None,
              "qn_ranking": 24,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter the initial",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 24
                }
              ]
            },
            {
              "title": "Date",
              "qno" : "Date 2",
              "is_required": True,
              "is_read_only": False,
              "position": 10,
              "others_status": None,
              "qn_ranking": 25,
              "answers": [
                {
                  "dtype": "datepicker",
                  "position": 1,
                  "placeholder": "DD/MM/YYYY",
                  "options": None,
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select a date to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": False,
                  "ranking": 25
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "category_name": "C. Encoding Information",
      "position": 4,
      "page": 4,
      "section": [
        {
          "section_name": "",
          "is_subheader": False,
          "position": 5,
          "qcount": 7,
          "anscount": 0,
          "questions": [
            {
              "title": "Date Encoded",
              "qno" : "Date Encoded",
              "is_required": True,
              "is_read_only": False,
              "position": 1,
              "others_status": None,
              "qn_ranking": 26,
              "answers": [
                {
                  "dtype": "datepicker",
                  "position": 1,
                  "placeholder": "DD/MM/YYYY",
                  "options": None,
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select a date to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": False,
                  "ranking": 26
                }
              ]
            },
            {
              "title": "Name of Encoder",
              "qno" : "Name of Encoder",
              "is_required": True,
              "is_read_only": False,
              "position": 2,
              "others_status": None,
              "qn_ranking": 27,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter the name",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 27
                }
              ]
            },
            {
              "title": "Initial of Encoder",
              "qno" : "Initial of Encoder",
              "is_required": True,
              "is_read_only": False,
              "position": 2,
              "others_status": None,
              "qn_ranking": 28,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter the name",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 28
                }
              ]
            },
            {
              "title": "Name of Supervisor",
              "qno" : "Name of Supervisor 2",
              "is_required": True,
              "is_read_only": False,
              "position": 3,
              "others_status": None,
              "qn_ranking": 29,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter the name of supervisor",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 29
                }
              ]
            },
            {
              "title": "Initial",
              "qno" : "Initial 3",
              "is_required": True,
              "is_read_only": False,
              "position": 4,
              "others_status": None,
              "qn_ranking": 30,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter the initial",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 30
                }
              ]
            },
            {
              "title": "Date",
              "qno" : "Date 3",
              "is_required": True,
              "is_read_only": False,
              "position": 4,
              "others_status": None,
              "qn_ranking": 31,
              "answers": [
                {
                  "dtype": "datepicker",
                  "position": 1,
                  "placeholder": "DD/MM/YYYY",
                  "options": None,
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select a date to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": False,
                  "ranking": 31
                }
              ]
            },
            {
              "title": "Barangay",
              "qno" : "Barangay 2",
              "is_required": True,
              "is_read_only": False,
              "position": 5,
              "others_status": None,
              "qn_ranking": 32,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Barangay",
                  "options": None,
                  "answer_value": "",
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 32
                }
              ]
            }
          ]
        }
      ]
    }
  ],
  "house_hold_member_section": "",
  "final_section": [
    {
      "category_name": "H1. Questions for Household",
      "position": 15,
      "page": 1,
      "section": [
        {
          "section_name": "",
          "is_subheader": False,
          "position": 21,
          "qcount": 5,
          "anscount": 0,
          "questions": [
            {
              "title": "45. Do you have own or amortize this housing unit occupied by your household or do you rent it, do you occupy it rent free with consent of owner or rent-free without consent of owner?",
              "qno" : "Q45",
              "is_required": True,
              "is_read_only": False,
              "position": 1,
              "others_status": False,
              "qn_ranking": 1,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select one",
                  "options": [
                    "Rent-free without consent of owner",
                    "Rent-free with consent of owner",
                    "Rented",
                    "Owned/being amortized"
                  ],
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select an option to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": False,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 1
                }
              ]
            },
            {
              "title": "46. Do you own or amortize this lot occupied by your household or do you rent it, do you occupy it rent-free with consent of owner or rent-free without consent of owner?",
              "qno" : "Q46",
              "is_required": True,
              "is_read_only": False,
              "position": 2,
              "others_status": False,
              "qn_ranking": 2,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select one",
                  "options": [
                    "Rent-free without consent of owner",
                    "Rent-free with consent of owner",
                    "Rented",
                    "Owned/being amortized"
                  ],
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select an option to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": False,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 2
                }
              ]
            },
            {
              "title": "47. What Types Of Fuel Does The Household Use For Lighting?",
              "qno" : "Q47",
              "is_required": True,
              "is_read_only": False,
              "position": 3,
              "others_status": False,
              "qn_ranking": 3,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select one",
                  "options": [
                    "None",
                    "Oil (vegetable, animal, others)",
                    "Liquefied petroleum gas (LPG)",
                    "Kerosene (gaas)",
                    "Electricity",
                    "Others"
                  ],
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select an option to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": False,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 3
                },
                {
                  "dtype": "other_textbox",
                  "position": 2,
                  "placeholder": "If others, please specify",
                  "options": None,
                  "answer_value": None,
                  "is_error": True,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 4
                }
              ]
            },
            {
              "title": "48. What kind of fuel does this household use most of the time for cooking?",
              "qno" : "Q48",
              "is_required": True,
              "is_read_only": False,
              "position": 4,
              "others_status": False,
              "qn_ranking": 4,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select one",
                  "options": [
                    "None",
                    "Wood",
                    "Charcoal",
                    "Liquefied petroleum gas (LPG)",
                    "Kerosene (gaas)",
                    "Electricity",
                    "Others"
                  ],
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select an option to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": False,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 5
                },
                {
                  "dtype": "other_textbox",
                  "position": 2,
                  "placeholder": "If others, please specify",
                  "options": None,
                  "answer_value": None,
                  "is_error": True,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 6
                }
              ]
            },
            {
              "title": "49. What is the household’s main source of drinking water?",
              "qno" : "Q49",
              "is_required": True,
              "is_read_only": False,
              "position": 5,
              "others_status": False,
              "qn_ranking": 5,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select one",
                  "options": [
                    "Lake, river, rain, others",
                    "Dug well",
                    "Unprotected spring",
                    "Protected spring",
                    "Peddler",
                    "Tubed/Piped shallow well",
                    "Shared, tubed/piped deep well",
                    "Own use, tubed/piped deep well",
                    "Shared, faucet community water system",
                    "Own use, faucet community water system",
                    "Bottled water",
                    "Others"
                  ],
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select an option to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": False,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 7
                },
                {
                  "dtype": "other_textbox",
                  "position": 2,
                  "placeholder": "If others, please specify",
                  "options": None,
                  "answer_value": None,
                  "is_error": True,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 8
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "category_name": "H2. Questions for Household",
      "position": 16,
      "page": 2,
      "section": [
        {
          "section_name": "",
          "is_subheader": False,
          "position": 22,
          "qcount": 5,
          "anscount": 0,
          "questions": [
            {
              "title": "50 A. How does your household usually dispose of your kitchen garbage such as leftover food, peeling of fruits and vegetables, fish and chicken entrails, and others ?",
              "qno" : "Q50A",
              "is_required": True,
              "is_read_only": False,
              "position": 1,
              "others_status": False,
              "qn_ranking": 6,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select one",
                  "options": [
                    "Feeding to animals",
                    "Burying",
                    "Composting",
                    "Burning",
                    "Dumping individual pit (not burned)",
                    "Picked-up by garbage truck"
                  ],
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select atleast one option to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": False,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 9
                }
              ]
            },
            {
              "title": "50 B. Do you segregate your garbage ?",
              "qno" : "Q50B",
              "is_required": True,
              "is_read_only": False,
              "position": 2,
              "others_status": True,
              "qn_ranking": 7,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select one",
                  "options": [
                    "Yes",
                    "No"
                  ],
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select an option to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": False,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 10
                }
              ]
            },
            {
              "title": "51. What type of toilet facility does this household use ?",
              "qno" : "Q51",
              "is_required": True,
              "is_read_only": False,
              "position": 3,
              "others_status": False,
              "qn_ranking": 8,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select one",
                  "options": [
                    "None",
                    "Open pit",
                    "Close pit",
                    "Water-sealed, other depository, shared",
                    "Water-sealed, other depository, exclusive",
                    "Water-sealed, sewer septic tank, shared",
                    "Water-sealed, sewer septic tank, exclusive",
                    "Others"
                  ],
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select an option to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": False,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 11
                },
                {
                  "dtype": "other_textbox",
                  "position": 2,
                  "placeholder": "If others, please specify",
                  "options": None,
                  "answer_value": None,
                  "is_error": True,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 12
                }
              ]
            },
            {
              "title": "52. Type of building / house (Do not ask, observation only)",
              "qno" : "Q52",
              "is_required": True,
              "is_read_only": False,
              "position": 4,
              "others_status": False,
              "qn_ranking": 9,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select one",
                  "options": [
                    "Single house",
                    "Duplex",
                    "Multi-unit residential (three units or more)",
                    "Commercial/industrial/agricultural",
                    "Institutional living quarter (hotel, hospital)",
                    "Other housing units (boat, cave, others)"
                  ],
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select an option to proceed.",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": False,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 13
                }
              ]
            },
            {
              "title": "53. Type of building / house (Do not ask, observation only)",
              "qno" : "Q53",
              "is_required": True,
              "is_read_only": False,
              "position": 4,
              "others_status": False,
              "qn_ranking": 10,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select one",
                  "options": [
                    "No walls",
                    "Makeshift/salvaged/improvised materials",
                    "Glass",
                    "Asbestos",
                    "Bamboo/Sawali/Cogon/Nipa",
                    "Galvanized iron/aluminum",
                    "Half concrete/brick/stone and half wood",
                    "Wood",
                    "Concrete/brick/stone",
                    "Others"
                  ],
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select an option to proceed.",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": False,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 14
                },
                {
                  "dtype": "other_textbox",
                  "position": 2,
                  "placeholder": "If others, please specify",
                  "options": None,
                  "answer_value": None,
                  "is_error": True,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 15
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "category_name": "H3. Questions for Household",
      "position": 17,
      "page": 3,
      "section": [
        {
          "section_name": "",
          "is_subheader": False,
          "position": 23,
          "qcount": 5,
          "anscount": 0,
          "questions": [
            {
              "title": "54. Do you have any female HH member who died in the past 12 months ? How old is she and what is the cause of her death ?",
              "qno" : "Q54",
              "is_required": True,
              "is_read_only": False,
              "position": 1,
              "others_status": False,
              "qn_ranking": 11,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select Yes / No",
                  "options": [
                    "Yes",
                    "No"
                  ],
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select an option to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": False,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 16
                },
                {
                  "dtype": "other_textbox",
                  "position": 1,
                  "placeholder": "Enter the age",
                  "options": None,
                  "answer_value": None,
                  "is_error": True,
                  "error_message": "Please enter a valid age to proceed",
                  "keyboard_type": "number",
                  "limitation": 2,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 17
                },
                {
                  "dtype": "other_textbox",
                  "position": 2,
                  "placeholder": "Enter the cause of death",
                  "options": None,
                  "answer_value": None,
                  "is_error": True,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 18
                }
              ]
            },
            {
              "title": "55. Do you have a child HH member below 5 years old who died in the past 12 months ? How old is she/ he What is the cause of her / his death ?",
              "qno" : "Q55",
              "is_required": True,
              "is_read_only": False,
              "position": 2,
              "others_status": False,
              "qn_ranking": 12,
              "answers": [
                {
                  "dtype": "selectbox",
                  "position": 1,
                  "placeholder": "Select Yes / No",
                  "options": [
                    "Yes",
                    "No"
                  ],
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please select an option to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": False,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 19
                },
                {
                  "dtype": "other_textbox",
                  "position": 1,
                  "placeholder": "Enter the age",
                  "options": None,
                  "answer_value": None,
                  "is_error": True,
                  "error_message": "Please enter a valid age to proceed",
                  "keyboard_type": "number",
                  "limitation": 2,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 20
                },
                {
                  "dtype": "other_selectbox",
                  "position": 2,
                  "placeholder": "Select sex",
                  "options": [
                    "Male",
                    "Female"
                  ],
                  "answer_value": None,
                  "is_error": True,
                  "error_message": "Please enter a valid sex to proceed",
                  "keyboard_type": None,
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 21
                },
                {
                  "dtype": "other_textbox",
                  "position": 3,
                  "placeholder": "Enter the cause of death",
                  "options": None,
                  "answer_value": None,
                  "is_error": True,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 22
                }
              ]
            },
            {
              "title": "56. What are the common diseases that causes death in this barangay ?",
              "qno" : "Q56",
              "is_required": True,
              "is_read_only": False,
              "position": 3,
              "others_status": None,
              "qn_ranking": 13,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter the disease name",
                  "options": None,
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 23
                }
              ]
            },
            {
              "title": "57. What do you think are the primary needs of this barangay ?",
              "qno" : "Q57",
              "is_required": True,
              "is_read_only": False,
              "position": 4,
              "others_status": None,
              "qn_ranking": 14,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter the disease name",
                  "options": None,
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please enter an answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 24
                }
              ]
            },
            {
              "title": "58. Where does your household intend to stay five years from now",
              "qno" : "Q58",
              "is_required": True,
              "is_read_only": False,
              "position": 5,
              "others_status": None,
              "qn_ranking": 15,
              "answers": [
                {
                  "dtype": "textbox",
                  "position": 1,
                  "placeholder": "Enter the Barangay",
                  "options": None,
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 25
                },
                {
                  "dtype": "textbox",
                  "position": 2,
                  "placeholder": "Enter the City/ Municipality",
                  "options": None,
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 26
                },
                {
                  "dtype": "textbox",
                  "position": 3,
                  "placeholder": "Enter the Province",
                  "options": None,
                  "answer_value": None,
                  "is_error": False,
                  "error_message": "Please enter a valid answer to proceed",
                  "keyboard_type": "text",
                  "limitation": None,
                  "show_dropdown_modal": None,
                  "show_time_picker": None,
                  "show_multi_dropdown_modal": None,
                  "show_picker": None,
                  "ranking": 27
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}

member_json = {
      "member_id": 1,
      "member_name": "",
      "member_passes": True,
      "member_completed_status": 0,
      "category": [
        {
          "_id": 1,
          "page": [
            {
              "category_name": "Demographic Characteristics",
              "position": 5,
              "page": 1,
              "section": [
                {
                  "section_name": "FOR ALL HOUSEHOLD MEMBERS",
                  "is_subheader": True,
                  "position": 6,
                  "qcount": 10,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "1.What is the name of the household member? (start from the HH head)",
                      "qno" : "Q1",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 1,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Enter the name of the head",
                          "options": None,
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid name to proceed.",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 1
                        }
                      ]
                    },
                    {
                      "title": "2. What is ___ ‘s relationship to HH head ?",
                      "qno" : "Q2",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 2,
                      "others_status": False,
                      "qn_ranking": 2,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select the relationship to household head",
                          "options": [
                            "Head",
                            "Spouse",
                            "Son",
                            "Daughter",
                            "Stepson",
                            "Stepdaughter",
                            "Son-in-law",
                            "Daughter-in-law",
                            "Grandson",
                            "Granddaughter",
                            "Father",
                            "Mother",
                            "Brother",
                            "Sister",
                            "Uncle",
                            "Aunt",
                            "Nephew",
                            "Niece",
                            "Other relative",
                            "Non-relative",
                            "Boarder",
                            "Domestic helper"
                          ],
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": False,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 2
                        }
                      ]
                    },
                    {
                      "title": "3. Is ___ male or female ?",
                      "qno" : "Q3",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 3,
                      "others_status": False,
                      "qn_ranking": 3,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select the gender",
                          "options": [
                            "Male",
                            "Female"
                          ],
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please select a gender to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": False,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 3
                        }
                      ]
                    },
                    {
                      "title": "4. How old is ___ as of his/her last birthday ?",
                      "qno" : "Q4", 
                      "is_required": True,
                      "is_read_only": False,
                      "position": 4,
                      "others_status": None,
                      "qn_ranking": 4,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Write the age as of last birthday",
                          "options": None,
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid age to proceed",
                          "keyboard_type": "number",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 4
                        }
                      ]
                    },
                    {
                      "title": "5. When was ___ born ?",
                      "qno" : "Q5",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 5,
                      "others_status": None,
                      "qn_ranking": 5,
                      "answers": [
                        {
                          "dtype": "age_picker",
                          "position": 1,
                          "placeholder": "MM/YYYY",
                          "options": None,
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": False,
                          "ranking": 5
                        }
                      ]
                    },
                    {
                      "title": "6. Place of birth? ",
                      "qno" : "Q6",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 6,
                      "others_status": None,
                      "qn_ranking": 6,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Enter the Province or City/ Municipality",
                          "options": None,
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid Province to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 6
                        },
                        {
                          "dtype": "textbox",
                          "position": 2,
                          "placeholder": "Enter the province",
                          "options": None,
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid province to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 7
                        }
                      ]
                    },
                    {
                      "title": "7. Is ___ a Filipino? If not, what is ___’s nationality?",
                      "qno" : "Q7",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 7,
                      "others_status": False,
                      "qn_ranking": 7,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select one",
                          "options": [
                            "Filipino",
                            "Non-Filipino"
                          ],
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Select the nationality to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": False,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 8
                        },
                        {
                          "dtype": "other_textbox",
                          "position": 2,
                          "placeholder": "Enter the nationality",
                          "options": None,
                          "answer_value": None,
                          "is_error": True,
                          "error_message": "Enter the nationality to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 9
                        }
                      ]
                    },
                    {
                      "title": "8. What is ___’s current marital status ?",
                      "qno" : "Q8",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 8,
                      "others_status": False,
                      "qn_ranking": 8,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select one",
                          "options": [
                            "Single",
                            "Married",
                            "Living-in",
                            "Widowed",
                            "Separated",
                            "Divorced",
                            "Unknown"
                          ],
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": False,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 10
                        }
                      ]
                    },
                    {
                      "title": "9. What is the religion of ___ ?",
                      "qno" : "Q9",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 9,
                      "others_status": None,
                      "qn_ranking": 9,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select one",
                          "options": [
                                      "Roman Catholic",
                                      "Protestant",
                                      "Iglesia ni Cristo",
                                      "Aglipay",
                                      "Islam",
                                      "Hinduism",
                                      "Jehovah's Witnesses",
                                      "Seventh-Day Adventists",
                                      "Christian",
                                      "Other Christian",
                                      "No religion"
                                    ],
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 11
                        }
                      ]
                    },
                    {
                      "title": "10. What is ___ ‘s ethnicity or is ___ a tagalog, Bicolana, Bisaya, etc ?",
                      "qno" : "Q10",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 10,
                      "others_status": None,
                      "qn_ranking": 10,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Enter the response",
                          "options": None,
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed.",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 12
                        }
                      ]
                    }
                  ],
                  "is_enable": True
                }
              ]
            }
          ]
        },
        {
          "_id": 2,
          "page": [
            {
              "category_name": "A. Demographic Characteristics",
              "position": 6,
              "page": 2,
              "section": [
                {
                  "section_name": "FOR 5 YRS & ABOVE",
                  "is_subheader": False,
                  "position": 7,
                  "qcount": 1,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "11. What is the highest level of education completed by ___?",
                      "qno" : "Q11",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 11,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select one",
                          "options": [
                            "No education",
                            "Pre-school",
                            "Elementary level",
                            "Elementary graduate",
                            "High school level",
                            "High school graduate",
                            "Junior HS",
                            "Junior HS graduate",
                            "Senior HS level",
                            "Senior HS graduate",
                            "Vocational/Tech ",
                            "College level",
                            "College graduate",
                            "Post-graduate"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 13
                        }
                      ]
                    }
                  ],
                  "is_enable": False
                },
                {
                  "section_name": "FOR 3-24 YEARS OLD",
                  "is_subheader": False,
                  "position": 8,
                  "qcount": 3,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "12. Is ___ currently enrolled ?",
                      "qno" : "Q12",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 12,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select one",
                          "options": [
                            "Yes, public",
                            "Yes, private",
                            "No"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 14
                        }
                      ]
                    },
                    {
                      "title": "13. What type of school is  ___ on ?",
                      "qno" : "Q13",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 2,
                      "others_status": None,
                      "qn_ranking": 13,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select one",
                          "options": [
                            "Pre-school",
                            "Elementary",
                            "Junior High School",
                            "Senior High School",
                            "Vocational/Technical",
                            "College/University"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 15
                        }
                      ]
                    },
                    {
                      "title": "14. In what city / municipality is ___ currently atttending school?",
                      "qno" : "Q14",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 3,
                      "others_status": None,
                      "qn_ranking": 14,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Enter the response",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 16
                        }
                      ]
                    }
                  ],
                  "is_enable": False
                }
              ]
            },
            {
              "category_name": "B. Economic Activity",
              "position": 7,
              "page": 2,
              "section": [
                {
                  "section_name": "FOR 15 YEARS OLD AND ABOVE",
                  "is_subheader": False,
                  "position": 9,
                  "qcount": 4,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "15.How much is ___’s monthly income?",
                      "qno" : "Q15",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 15,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Enter the response",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "number",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 17
                        }
                      ]
                    },
                    {
                      "title": "16. What is the major source of  ___’s income ?",
                      "qno" : "Q16",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 2,
                      "others_status": None,
                      "qn_ranking": 16,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select one",
                          "options": [
                            "Employment",
                            "Business",
                            "Remittance",
                            "Investments",
                            "Others"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 18
                        },
                        {
                          "dtype": "other_textbox",
                          "position": 2,
                          "placeholder": "For others",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 19
                        }
                      ]
                    },
                    {
                      "title": "17. What is the status of  ___’s work /business ?",
                      "qno" : "Q17", 
                      "is_required": True,
                      "is_read_only": False,
                      "position": 3,
                      "others_status": None,
                      "qn_ranking": 17,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select one",
                          "options": [
                            "Permanent Work",
                            "Casual Work",
                            "Contractual Work",
                            "Individually Owned Business",
                            "Shared/Partnership Business",
                            "Corporate Business"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 20
                        }
                      ]
                    },
                    {
                      "title": " 18. In what city / municipality is ___’s work/business located ?",
                      "qno" : "Q18",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 4,
                      "others_status": None,
                      "qn_ranking": 18,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Enter the response",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 21
                        }
                      ]
                    }
                  ],
                  "is_enable": False
                }
              ]
            }
          ]
        },
        {
          "_id": 3,
          "page": [
            {
              "category_name": "C. Health Information",
              "position": 8,
              "page": 3,
              "section": [
                {
                  "section_name": "FOR 0 TO 11 MONTHS OLD",
                  "is_subheader": False,
                  "position": 10,
                  "qcount": 3,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "19. Where was ___ delivered ?",
                      "qno" : "Q19",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 19,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Enter the response",
                          "options": [
                            "Public hospital",
                            "Private hospital",
                            "Lying-in clinic",
                            "Home",
                            "Others"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 22
                        },
                        {
                          "dtype": "other_textbox",
                          "position": 2,
                          "placeholder": "For others",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 23
                        }
                      ]
                    },
                    {
                      "title": "20. Who attended in the delivery of ___ ?",
                      "qno" : "Q20", 
                      "is_required": True,
                      "is_read_only": False,
                      "position": 2,
                      "others_status": None,
                      "qn_ranking": 20,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Enter the response",
                          "options": [
                            "Doctor",
                            "Nurse",
                            "Midwife",
                            "Hilot",
                            "Others"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 24
                        },
                        {
                          "dtype": "other_textbox",
                          "position": 2,
                          "placeholder": "For others",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 25
                        }
                      ]
                    },
                    {
                      "title": "21. What is the last vaccine received by ___ ?",
                      "qno" : "Q21",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 3,
                      "others_status": None,
                      "qn_ranking": 21,
                      "answers": [
                        {
                          "dtype": "textarea",
                          "position": 1,
                          "placeholder": "Enter the vaccine last received by the infant. Mother / Baby Book or Immunization card may be used as reference",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 26
                        }
                      ]
                    }
                  ],
                  "is_enable": False
                },
                {
                  "section_name": "FOR WOMEN 10 TO 54 YEARS",
                  "is_subheader": False,
                  "position": 11,
                  "qcount": 4,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "22. How many pregnancies does ___  had ? How many children are still living?",
                      "qno" : "Q22",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 22,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Select the number of pregnancies",
                          "options": [

                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "number",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 27
                        },
                        {
                          "dtype": "textbox",
                          "position": 2,
                          "placeholder": "How many are still living as time of interview",
                          "options": [

                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "number",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 28
                        }
                      ]
                    },
                    {
                      "title": "23. What family planning method does ___  and partner currently use ?",
                      "qno" : "Q23",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 2,
                      "others_status": None,
                      "qn_ranking": 23,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Enter the response",
                          "options": [
                            "Female sterilization/Ligation",
                            "Male sterilization/Vasectomy",
                            "IUD",
                            "Injectables",
                            "Implants",
                            "Pill",
                            "Condom",
                            "Modern natural FP",
                            "Lactational Amenorrhea Method (LAM)",
                            "Traditional",
                            "Not Applicable"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 29
                        }
                      ]
                    },
                    {
                      "title": "24. If using FP, where did they obtain the FP ?",
                      "qno" : "Q24",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 3,
                      "others_status": None,
                      "qn_ranking": 24,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Enter the response",
                          "options": [
                            "Government hospital",
                            "RHU/Health center",
                            "Brgy. Health Station",
                            "Private hospital",
                            "Pharmacy",
                            "Others"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 30
                        },
                        {
                          "dtype": "other_textbox",
                          "position": 2,
                          "placeholder": "For others",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 31
                        }
                      ]
                    },
                    {
                      "title": "25. Does ____ and partner intend to use FP method ?",
                      "qno" : "Q25",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 4,
                      "others_status": None,
                      "qn_ranking": 25,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Enter the response",
                          "options": [
                            "Yes",
                            "No",
                            "Not Applicable"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 32
                        },
                        {
                          "dtype": "textbox",
                          "position": 2,
                          "placeholder": "FP method or reason",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 33
                        }
                      ]
                    }
                  ],
                  "is_enable": False
                }
              ]
            }
          ]
        },
        {
          "_id": 4,
          "page": [
            {
              "category_name": "C. Health Information",
              "position": 9,
              "page": 4,
              "section": [
                {
                  "section_name": "FOR ALL HOUSEHOLD MEMBERS",
                  "is_subheader": True,
                  "position": 12,
                  "qcount": 4,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "26. What is the primary health insurance ____ have ?",
                      "qno" : "Q26",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": False,
                      "qn_ranking": 26,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select One",
                          "options": [
                            "PhilHealth paying member",
                            "PhilHealth dependent of paying member",
                            "PhilHealth indigent member",
                            "PhilHealth dependent of indigent member",
                            "GSIS",
                            "SSS",
                            "Private/HMO",
                            "Others"
                          ],
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": False,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 34
                        },
                        {
                          "dtype": "other_textbox",
                          "position": 2,
                          "placeholder": "For others",
                          "options": None,
                          "answer_value": None,
                          "is_error": True,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 35
                        }
                      ]
                    },
                    {
                      "title": "27. What facility did ____ visit in the past 12 months ?",
                      "qno" : "Q27",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 2,
                      "others_status": False,
                      "qn_ranking": 27,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select One",
                          "options": [
                            "Government hospital",
                            "RHU/Health center",
                            "Brgy. Health Station",
                            "Private hospital",
                            "Private clinic",
                            "Pharmacy",
                            "Hilot/Herbalist",
                            "Others"
                          ],
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": False,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 36
                        },
                        {
                          "dtype": "other_textbox",
                          "position": 2,
                          "placeholder": "For others",
                          "options": None,
                          "answer_value": None,
                          "is_error": True,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 37
                        }
                      ]
                    },
                    {
                      "title": "28. What is the reason for the visit in health facility ?",
                      "qno" : "Q28",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 3,
                      "others_status": False,
                      "qn_ranking": 28,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select One",
                          "options": [
                            "Sick/Injured",
                            "Prenatal/Postnatal",
                            "Gave birth",
                            "Dental",
                            "Medical check-up",
                            "Medical requirement",
                            "NHTS/CCT/4Ps requirement",
                            "Others"
                          ],
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": False,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 38
                        },
                        {
                          "dtype": "other_textbox",
                          "position": 2,
                          "placeholder": "For others",
                          "options": None,
                          "answer_value": None,
                          "is_error": True,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 39
                        }
                      ]
                    },
                    {
                      "title": "29. Does the household member have any disability/ies? What is the disability ?",
                      "qno" : "Q29",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 4,
                      "others_status": None,
                      "qn_ranking": 29,
                      "answers": [
                        {
                          "dtype": "textarea",
                          "position": 1,
                          "placeholder": "If with disability, write the disability type, if no write None",
                          "options": None,
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 40
                        }
                      ]
                    }
                  ],
                  "is_enable": True
                }
              ]
            },
            {
              "category_name": "D. Socio-Civic Participation",
              "position": 10,
              "page": 4,
              "section": [
                {
                  "section_name": "FOR 10 & ABOVE",
                  "is_subheader": False,
                  "position": 13,
                  "qcount": 1,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "30. Is there a member of the HH that is a solo parent ? Is he/she registered ?",
                      "qno" : "Q30",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 30,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select One",
                          "options": [
                            "Registered Solo parent",
                            "Non-Solo Parent",
                            "Unregistered Solo Parent"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 41
                        }
                      ]
                    }
                  ],
                  "is_enable": False
                },
                {
                  "section_name": "FOR 60 & ABOVE",
                  "is_subheader": False,
                  "position": 14,
                  "qcount": 1,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "31. Is ___ a registered senior citizen ?",
                      "qno" : "Q31",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 31,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select One",
                          "options": [
                            "Yes",
                            "No"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 42
                        }
                      ]
                    }
                  ],
                  "is_enable": False
                },
                {
                  "section_name": "FOR 15 & ABOVE",
                  "is_subheader": False,
                  "position": 15,
                  "qcount": 1,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "32. In what barangay is ___ a registered voter ?",
                      "qno" : "Q32",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 32,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Enter the barangay",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 43
                        }
                      ]
                    }
                  ],
                  "is_enable": False
                }
              ]
            }
          ]
        },
        {
          "_id": 5,
          "page": [
            {
              "category_name": "E. Migration Information",
              "position": 11,
              "page": 5,
              "section": [
                {
                  "section_name": "FOR ALL HOUSEHOLD MEMBERS",
                  "is_subheader": True,
                  "position": 16,
                  "qcount": 4,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "33. In what city / municipality did ____ reside  five years ago ?",
                      "qno" : "Q33",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 33,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Enter city / Municipality",
                          "options": None,
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 44
                        },
                        {
                          "dtype": "textbox",
                          "position": 2,
                          "placeholder": "Enter barangay",
                          "options": None,
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 45
                        }
                      ]
                    },
                    {
                      "title": "34. In what barangay and city / municipality did ____ reside six months ago ?",
                      "qno" : "Q34",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 2,
                      "others_status": None,
                      "qn_ranking": 34,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Enter city / Municipality",
                          "options": None,
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 46
                        },
                        {
                          "dtype": "textbox",
                          "position": 2,
                          "placeholder": "Enter barangay",
                          "options": None,
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 47
                        }
                      ]
                    },
                    {
                      "title": "35. How long is ____ been staying in this barangay ? No. of years / No. of months ?",
                      "qno" : "Q35",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 3,
                      "others_status": None,
                      "qn_ranking": 35,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Select the number of years",
                          "options": None,
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "number",
                          "limitation": 4,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 48
                        },
                        {
                          "dtype": "textbox",
                          "position": 2,
                          "placeholder": "Select the number of months",
                          "options": None,
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "number",
                          "limitation": 2,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 49
                        }
                      ]
                    },
                    {
                      "title": "36. Indicate if Non - migrant , Migrant or Transient ?",
                      "qno" : "Q36",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 4,
                      "others_status": False,
                      "qn_ranking": 36,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select one",
                          "options": [
                            "Non-Migrant",
                            "Migrant",
                            "Transient"
                          ],
                          "answer_value": "",
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": False,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 50
                        }
                      ]
                    }
                  ],
                  "is_enable": True
                },
                {
                  "section_name": "FOR MIGRANTS AND TRANSIENTS",
                  "is_subheader": False,
                  "position": 17,
                  "qcount": 2,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "37. When did ____ transfer in the barangay ? MM / YYYY  ?",
                      "qno" : "Q37",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 37,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "MM",
                          "options": None,
                          "answer_value": None,
                          "is_error": True,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": "number",
                          "limitation": 2,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 51
                        },
                        {
                          "dtype": "textbox",
                          "position": 2,
                          "placeholder": "YYYY",
                          "options": None,
                          "answer_value": None,
                          "is_error": True,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": "number",
                          "limitation": 4,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 52
                        }
                      ]
                    },
                    {
                      "title": "38. What are the reasons why ____ left his/her previous residence ?",
                      "qno" : "Q38",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 2,
                      "others_status": None,
                      "qn_ranking": 38,
                      "answers": [
                        {
                          "dtype": "multiselectbox",
                          "position": 1,
                          "placeholder": "Select one",
                          "options": [
                            "Lack of employment",
                            "Perception of better income in other place",
                            "Schooling",
                            "Presence of relatives and friends in other place",
                            "Employment/Job Relocation",
                            "Disaster-related Relocation",
                            "Retirement",
                            "To live with Parents",
                            "To live with Children",
                            "Marriage",
                            "Annulment/Divorce/ Separation",
                            "Commuting-related Reasons",
                            "Health-related Reasons",
                            "Peace and Security",
                            "Others"
                          ],
                          "answer_value": None,
                          "is_error": True,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 53
                        },
                        {
                          "dtype": "other_textbox",
                          "position": 2,
                          "placeholder": "Others",
                          "options": None,
                          "answer_value": None,
                          "is_error": True,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 54
                        }
                      ]
                    }
                  ],
                  "is_enable": False
                }
              ]
            }
          ]
        },
        {
          "_id": 6,
          "page": [
            {
              "category_name": "E. Migration Information",
              "position": 12,
              "page": 6,
              "section": [
                {
                  "section_name": "FOR MIGRANTS AND TRANSIENTS",
                  "is_subheader": True,
                  "position": 18,
                  "qcount": 3,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "39. Does ____ plan to return to previous residence ? When ?",
                      "qno" : "Q39",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 39,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select Yes / No",
                          "options": [
                            "Yes",
                            "No"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 55
                        },
                        {
                          "dtype": "textbox",
                          "position": 2,
                          "placeholder": "Enter the response",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 56
                        },
                        {
                          "dtype": "datepicker",
                          "position": 3,
                          "placeholder": "Select date",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Select a date to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 57
                        }
                      ]
                    },
                    {
                      "title": "40. What are the reasons why ____ transferred in this barangay?",
                      "qno" : "Q40",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 2,
                      "others_status": None,
                      "qn_ranking": 40,
                      "answers": [
                        {
                          "dtype": "multiselectbox",
                          "position": 1,
                          "placeholder": "Select one",
                          "options": [
                            "Availability of jobs",
                            "Higher wage",
                            "Presence of schools or universities",
                            "Presence of relatives and friends in other place",
                            "Housing",
                            "Others"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 58
                        },
                        {
                          "dtype": "other_textbox",
                          "position": 2,
                          "placeholder": "Others",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 59
                        }
                      ]
                    },
                    {
                      "title": "41. Until when does ___ intend to stay in this barangay?",
                      "qno" : "Q41",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 3,
                      "others_status": None,
                      "qn_ranking": 41,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Enter the response",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 60
                        }
                      ]
                    }
                  ],
                  "is_enable": False
                }
              ]
            },
            {
              "category_name": "F. Community Tax Certificate",
              "position": 13,
              "page": 6,
              "section": [
                {
                  "section_name": "FOR 18 & ABOVE",
                  "is_subheader": True,
                  "position": 19,
                  "qcount": 2,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "42 A. Does ___ have a valid CTC ?",
                      "qno" : "Q42A",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 42,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select Yes / No",
                          "options": [
                            "Yes",
                            "No"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 61
                        },
                        {
                          "dtype": "other_textbox",
                          "position": 2,
                          "placeholder": "If no, enter the response",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 62
                        }
                      ]
                    },
                    {
                      "title": "42 B. Was the CTC issued in this barangay ?",
                      "qno" : "Q42B",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 2,
                      "others_status": None,
                      "qn_ranking": 43,
                      "answers": [
                        {
                          "dtype": "selectbox",
                          "position": 1,
                          "placeholder": "Select one",
                          "options": [
                            "Yes",
                            "No"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select an option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 63
                        }
                      ]
                    }
                  ],
                  "is_enable": False
                }
              ]
            },
            {
              "category_name": "G. Skill Development",
              "position": 14,
              "page": 6,
              "section": [
                {
                  "section_name": "FOR 15 & ABOVE",
                  "is_subheader": True,
                  "position": 20,
                  "qcount": 2,
                  "anscount": 0,
                  "questions": [
                    {
                      "title": "43. What type of skills development training is ____ interested to join in?",
                      "qno" : "Q43",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 1,
                      "others_status": None,
                      "qn_ranking": 44,
                      "answers": [
                        {
                          "dtype": "textbox",
                          "position": 1,
                          "placeholder": "Enter the response",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 64
                        }
                      ]
                    },
                    {
                      "title": "44. What type of skills do you have?",
                      "qno" : "Q44",
                      "is_required": True,
                      "is_read_only": False,
                      "position": 2,
                      "others_status": None,
                      "qn_ranking": 45,
                      "answers": [
                        {
                          "dtype": "multiselectbox",
                          "position": 1,
                          "placeholder": "Select one",
                          "options": [
                            "Refrigeration and Airconditioning",
                            "Automotive/Heavy Equipment Servicing",
                            "Metal Worker",
                            "Building Wiring Installation",
                            "Heavy Equipment Operation",
                            "Plumbing",
                            "Welding",
                            "Carpentry",
                            "Baking",
                            "Dressmaking",
                            "Linguist",
                            "Computer Graphics",
                            "Painting",
                            "Beauty Care",
                            "Commercial Cooking",
                            "Housekeeping",
                            "Massage Therapy",
                            "Others"
                          ],
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please select atleast one option to proceed",
                          "keyboard_type": None,
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 65
                        },
                        {
                          "dtype": "other_textbox",
                          "position": 2,
                          "placeholder": "Others",
                          "options": None,
                          "answer_value": None,
                          "is_error": False,
                          "error_message": "Please enter a valid answer to proceed",
                          "keyboard_type": "text",
                          "limitation": None,
                          "show_dropdown_modal": None,
                          "show_time_picker": None,
                          "show_multi_dropdown_modal": None,
                          "show_picker": None,
                          "ranking": 66
                        }
                      ]
                    }
                  ],
                  "gender": "Male",
                  "is_enable": False,
                  "age": 1
                }
              ]
            }
          ]
        }
      ]
    }