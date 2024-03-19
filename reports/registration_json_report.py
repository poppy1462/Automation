[
{"keyword": "Feature", "name": "Registration functionality", "tags": ["wip"], "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:2", "status": "failed", "elements": [{"type": "scenario", "keyword": "Scenario", "name": "User fills out all the fields", "tags": ["positive"], "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:5", "steps": [{"keyword": "When", "step_type": "when", "name": "User fills out all the fields", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:6", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:17", "arguments": []}, "result": {"status": "passed", "duration": 1.0868239402770996}}, {"keyword": "And", "step_type": "when", "name": "User chooses United States from the Country dropdown and Illinois from the Region/State dropdown", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:7", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:60", "arguments": []}, "result": {"status": "passed", "duration": 0.3800060749053955}}, {"keyword": "And", "step_type": "when", "name": "User clicks the checkmark", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:8", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:68", "arguments": []}, "result": {"status": "passed", "duration": 0.12521886825561523}}, {"keyword": "And", "step_type": "when", "name": "User clicks the Continue button", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:9", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:74", "arguments": []}, "result": {"status": "passed", "duration": 0.4489750862121582}}, {"keyword": "Then", "step_type": "then", "name": "Account created title is shown", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:10", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:80", "arguments": []}, "result": {"status": "failed", "duration": 0.08490800857543945, "error_message": ["Traceback (most recent call last):", "  File \"/Users/anastasiatskhay/Desktop/PythonProjects/lib/python3.9/site-packages/behave/model.py\", line 1329, in run", "    match.run(runner.context)", "  File \"/Users/anastasiatskhay/Desktop/PythonProjects/lib/python3.9/site-packages/behave/matchers.py\", line 98, in run", "    self.func(context, *args, **kwargs)", "  File \"BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py\", line 83, in verify_account_created_title", "    assert registration_page.get_form_title() == \"Your Account Has Been Created!\"", "AssertionError"]}}], "status": "failed"}, {"type": "scenario", "keyword": "Scenario", "name": "User fills out all the fields except the Address section", "tags": ["negative"], "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:13", "steps": [{"keyword": "When", "step_type": "when", "name": "User fills out all the fields except the Address section", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:14", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:46", "arguments": []}, "result": {"status": "passed", "duration": 1.062356948852539}}, {"keyword": "And", "step_type": "when", "name": "User chooses United States from the Country dropdown and Illinois from the Region/State dropdown", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:15", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:60", "arguments": []}, "result": {"status": "passed", "duration": 0.3959639072418213}}, {"keyword": "And", "step_type": "when", "name": "User clicks the checkmark", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:16", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:68", "arguments": []}, "result": {"status": "passed", "duration": 0.13497614860534668}}, {"keyword": "And", "step_type": "when", "name": "User clicks the Continue button", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:17", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:74", "arguments": []}, "result": {"status": "passed", "duration": 0.4352560043334961}}, {"keyword": "Then", "step_type": "then", "name": "Address alert is shown", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:18", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:86", "arguments": []}, "result": {"status": "passed", "duration": 0.08642411231994629}}], "status": "passed"}, {"type": "scenario", "keyword": "Scenario", "name": "User has an existing account", "tags": ["negative", "skip"], "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:21", "steps": [{"keyword": "When", "step_type": "when", "name": "Existing user fills out all the fields", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:22", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:32", "arguments": []}, "result": {"status": "passed", "duration": 1.2440850734710693}}, {"keyword": "And", "step_type": "when", "name": "User chooses United States from the Country dropdown and Illinois from the Region/State dropdown", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:23", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:60", "arguments": []}, "result": {"status": "passed", "duration": 0.34815001487731934}}, {"keyword": "And", "step_type": "when", "name": "User clicks the checkmark", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:24", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:68", "arguments": []}, "result": {"status": "passed", "duration": 0.13782286643981934}}, {"keyword": "And", "step_type": "when", "name": "User clicks the Continue button", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:25", "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:74", "arguments": []}, "result": {"status": "passed", "duration": 0.4497799873352051}}, {"keyword": "Then", "step_type": "then", "name": "Existing account alert is shown", "location": "BrainBucketTesting/BDDBehave/registrationtests/registration.feature:26", "text": ["When you select scenarios by one tag:", "behave **/registration.feature --tags=@wip", "When you select scenarios that have one or another tag:", "behave **/registration.feature --tags=@skip,@positive", "When you select scenarios that have 2 tags:", "behave **/registration.feature --tags=@negative --tags=@skip", "When you disable scenarios that have a specific tag:", "behave **/registration.feature --tags=~@negative"], "match": {"location": "BrainBucketTesting/BDDBehave/registrationtests/steps/registrationsteps.py:92", "arguments": []}, "result": {"status": "passed", "duration": 0.08377814292907715}}], "status": "passed"}]}
]