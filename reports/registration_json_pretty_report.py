[
{
  "elements": [
    {
      "keyword": "Scenario",
      "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:5",
      "name": "User fills out all the fields",
      "status": "failed",
      "steps": [
        {
          "keyword": "When",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:6",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:17"
          },
          "name": "User fills out all the fields",
          "result": {
            "duration": 1.1413078308105469,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:7",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:60"
          },
          "name": "User chooses United States from the Country dropdown and Illinois from the Region/State dropdown",
          "result": {
            "duration": 0.3578379154205322,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:8",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:68"
          },
          "name": "User clicks the checkmark",
          "result": {
            "duration": 0.12826991081237793,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:9",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:74"
          },
          "name": "User clicks the Continue button",
          "result": {
            "duration": 0.473146915435791,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "Then",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:10",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:80"
          },
          "name": "Account created title is shown",
          "result": {
            "duration": 0.07600903511047363,
            "error_message": [
              "Traceback (most recent call last):",
              "  File \"/Users/anastasiatskhay/Desktop/PythonProjects/lib/python3.9/site-packages/behave/model.py\", line 1329, in run",
              "    match.run(runner.context)",
              "  File \"/Users/anastasiatskhay/Desktop/PythonProjects/lib/python3.9/site-packages/behave/matchers.py\", line 98, in run",
              "    self.func(context, *args, **kwargs)",
              "  File \"BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py\", line 83, in verify_account_created_title",
              "    assert registration_page.get_form_title() == \"Your Account Has Been Created!\"",
              "AssertionError"
            ],
            "status": "failed"
          },
          "step_type": "then"
        }
      ],
      "tags": [
        "positive"
      ],
      "type": "scenario"
    },
    {
      "keyword": "Scenario",
      "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:13",
      "name": "User fills out all the fields except the Address section",
      "status": "passed",
      "steps": [
        {
          "keyword": "When",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:14",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:46"
          },
          "name": "User fills out all the fields except the Address section",
          "result": {
            "duration": 1.063615083694458,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:15",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:60"
          },
          "name": "User chooses United States from the Country dropdown and Illinois from the Region/State dropdown",
          "result": {
            "duration": 0.38663387298583984,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:16",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:68"
          },
          "name": "User clicks the checkmark",
          "result": {
            "duration": 0.15755581855773926,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:17",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:74"
          },
          "name": "User clicks the Continue button",
          "result": {
            "duration": 0.4762561321258545,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "Then",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:18",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:86"
          },
          "name": "Address alert is shown",
          "result": {
            "duration": 0.09048914909362793,
            "status": "passed"
          },
          "step_type": "then"
        }
      ],
      "tags": [
        "negative"
      ],
      "type": "scenario"
    },
    {
      "keyword": "Scenario",
      "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:21",
      "name": "User has an existing account",
      "status": "passed",
      "steps": [
        {
          "keyword": "When",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:22",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:32"
          },
          "name": "Existing user fills out all the fields",
          "result": {
            "duration": 1.2738008499145508,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:23",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:60"
          },
          "name": "User chooses United States from the Country dropdown and Illinois from the Region/State dropdown",
          "result": {
            "duration": 0.3298380374908447,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:24",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:68"
          },
          "name": "User clicks the checkmark",
          "result": {
            "duration": 0.1256110668182373,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:25",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:74"
          },
          "name": "User clicks the Continue button",
          "result": {
            "duration": 0.43950486183166504,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "Then",
          "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:26",
          "match": {
            "arguments": [],
            "location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:92"
          },
          "name": "Existing account alert is shown",
          "result": {
            "duration": 0.09291481971740723,
            "status": "passed"
          },
          "step_type": "then",
          "text": [
            "When you select scenarios by one tag:",
            "behave **/registration.feature --tags=@wip",
            "When you select scenarios that have one or another tag:",
            "behave **/registration.feature --tags=@skip,@positive",
            "When you select scenarios that have 2 tags:",
            "behave **/registration.feature --tags=@negative --tags=@skip",
            "When you disable scenarios that have a specific tag:",
            "behave **/registration.feature --tags=~@negative"
          ]
        }
      ],
      "tags": [
        "negative",
        "skip"
      ],
      "type": "scenario"
    }
  ],
  "keyword": "Feature",
  "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:2",
  "name": "Registration functionality",
  "status": "failed",
  "tags": [
    "wip"
  ]
}
]
