class RubricsWithFewShotExamples:
    def __init__(self):
        # Prompt, Rubric and Task Decomposition for Dataset 1
        self.Set_1_Prompt = """
        More and more people use computers, but not everyone agrees that this benefits society. Those who support advances in technology believe that computers have a positive effect on people. They teach hand-eye coordination, give people the ability to learn about faraway places and people, and even allow people to talk online with other people. Others have different ideas. Some experts are concerned that people are spending too much time on their computers and less time exercising, enjoying nature, and interacting with family and friends. 
        \n Write a letter to your local newspaper in which you state your opinion on the effects computers have on people. Persuade the readers to agree with you.
        """
        self.Set_1_Rubric = """
        Evaluation Rubric for Persuasive Writing
        1. Holistic Scoring:
        - First Draft Context: Remember that student responses are first drafts written in forty-five minutes, reacting to a prompt designed to elicit persuasive writing.
        - Overall Impression: As a trained reader, score each timed response holistically, determining a score based on the overall impression gained from a single reading.
        2. Six-Point Scale Rubric:
        - Understanding the Rubric: Utilize the six-point scale rubric provided. Each score point includes an overall statement capturing the essence of responses at that level.
        - Evaluating Key Elements: Consider the elements of the response that are typical for each score point:
        a) Elaboration
        b) Organization
        c) Fluency
        d) Audience Awareness
        - Holistic Judgment: Be mindful that individual responses may excel in some areas while needing improvement in others. The listed features cannot perfectly describe every response in a score-point category. Use your professional judgment to assess the overall quality.
        3. Errors Not Penalized:
        - Focus on Content: Do not consider errors in spelling, punctuation, grammar, and usage as part of the scoring criteria.
        - Incomplete Responses: Assign scores based on the work the student has completed, even if the response appears unfinished.
        - Assumption of Revision Ability: Since the writing sample is a timed response, assume that errors and omissions could have been corrected if the student had more time to revise and edit.
        - Reading Through Errors: As a trained reader, you should look past these errors when scoring, focusing on the student's overall writing ability and the effectiveness of their persuasive techniques.
        Specific Scoring Guide for the Rubric:
        Score Point 1: An undeveloped response that may take a position but offers no more than very minimal support. Typical elements:
        - Contains few or vague details.
        - Is awkward and fragmented.
        - May be difficult to read and understand.
        - May show no awareness of audience.
        Score Point 2: An under-developed response that may or may not take a position. Typical elements:
        - Contains only general reasons with unelaborated and/or list-like details.
        - Shows little or no evidence of organization.
        - May be awkward and confused or simplistic.
        - May show little awareness of audience.
        Score Point 3: A minimally-developed response that may take a position, but with inadequate support and details. Typical elements:
        - Has reasons with minimal elaboration and more general than specific details.
        - Shows some organization.
        - May be awkward in parts with few transitions.
        - Shows some awareness of audience.
        Score Point 4: A somewhat-developed response that takes a position and provides adequate support. Typical elements:
        - Has adequately elaborated reasons with a mix of general and specific details.
        - Shows satisfactory organization.
        - May be somewhat fluent with some transitional language.
        - Shows adequate awareness of audience.
        Score Point 5: A developed response that takes a clear position and provides reasonably persuasive support. Typical elements:
        - Has moderately well elaborated reasons with mostly specific details.
        - Exhibits generally strong organization.
        - May be moderately fluent with transitional language throughout.
        - May show a consistent awareness of audience.
        Score Point 6: A well-developed response that takes a clear and thoughtful position and provides persuasive support. Typical elements:
        - Has fully elaborated reasons with specific details.
        - Exhibits strong organization.
        - Is fluent and uses sophisticated transitional language.
        - May show a heightened awareness of audience.
        """
        self.Set_1_Task_Decomposition = """
        1. **Carefully read** the **essay prompt**, **scoring guideline**, and the **student's essay**.
        2. **Analyze** the student's essay in relation to the rubrics, focusing on the four dimensions:
        a) **Elaboration**
        b) **Organization**
        c) **Fluency**
        d) **Audience Awareness**
        In the **Explanations** section for each dimensions:
        - **Identify specific elements** from the essay that correspond to the rubrics.
        - Provide **detailed and evidence-based explanations** for your observations.
          The Explanations for each dimension should be as detailed as possible.
        3. **Assign appropriate scores** for each dimension based on your analysis.
        4. **Determine the final score** for the essay by considering the individual dimension scores and the overall quality of the essay.
        5. **Present your evaluation** **STRICTLY** in the following format:`
        - Explanations: ..., Elaboration Score: ...
        - Explanations: ..., Organization Score: ...
        - Explanations: ..., Fluency Score: ...
        - Explanations: ..., Audience Awareness Score: ...
        - Your final evaluation:
        - [Elaboration Score: ..., Organization Score: ..., Fluency Score: ..., Audience Awareness Score: ...]
        - [Final Score: ...]`
        """
        ###

        # Source, Prompt, Rubric and Task Decomposition for Dataset 2
        self.Set_2_Prompt = """
        This is a Source Dependent Responses Writing Task, you need to response to the following prompt based on the provided source.
        Source:`
        from Home: The Blueprints of Our Lives
        My parents, originally from Cuba, arrived in the United States in 1956. After living for a year in a furnished one-room apartment, twenty-one-year-old Rawedia Maria and twenty-seven-year-old Narciso Rodriguez, Sr., could afford to move into a modest, three-room apartment I would soon call home.
        In 1961, I was born into this simple house, situated in a two-family, blond-brick building in the Ironbound section of Newark, New Jersey. Within its walls, my young parents created our traditional Cuban home, the very heart of which was the kitchen. My parents both shared cooking duties and unwittingly passed on to me their rich culinary skills and a love of cooking that is still with me today (and for which I am eternally grateful). Passionate Cuban music (which I adore to this day) filled the air, mixing with the aromas of the kitchen. Here, the innocence of childhood, the congregation of family and friends, and endless celebrations that encompassed both, formed the backdrop to life in our warm home.
        Growing up in this environment instilled in me a great sense that “family” had nothing to do with being a blood relative. Quite the contrary, our neighborhood was made up of mostly Spanish, Cuban, and Italian immigrants at a time when overt racism was the norm and segregation prevailed in the United States. In our neighborhood, despite customs elsewhere, all of these cultures came together in great solidarity and friendship. It was a close-knit community of honest, hardworking immigrants who extended a hand to people who, while not necessarily their own kind, were clearly in need.
        Our landlord and his daughter, Alegria (my babysitter and first friend), lived above us, and Alegria graced our kitchen table for meals more often than not. Also at the table were Sergio and Edelmira, my surrogate grandparents who lived in the basement apartment. (I would not know my “real” grandparents, Narciso the Elder and Consuelo, until 1970 when they were allowed to leave Cuba.) My aunts Bertha and Juanita and my cousins Arnold, Maria, and Rosemary also all lived nearby and regularly joined us at our table. Countless extended family members came and went — and there was often someone staying with us temporarily until they were able to get back on their feet. My parents always kept their arms and their door open to the many people we considered family, knowing that they would do the same for us.
        My mother and father had come to this country with such courage, without any knowledge of the language or the culture. They came selflessly, as many immigrants do, to give their children a better life, even though it meant leaving behind their families, friends, and careers in the country they loved. They struggled both personally and financially, braving the harsh northern winters while yearning for their native tropics and facing cultural hardships. The barriers to work were strong and high, and my parents both had to accept that they might not be able to find the kind of jobs they deserved. In Cuba, Narciso, Sr., had worked in a laboratory and Rawedia Maria had studied chemical engineering. In the United States, they had to start their lives over entirely, taking whatever work they could find. The faith that this struggle would lead them and their children to better times drove them to endure these hard times.
        I will always be grateful to my parents for their love and sacrifice. I’ve often told them that what they did was a much more courageous thing than I could have ever done. I’ve often told them of my admiration for their strength and perseverance, and I’ve thanked them repeatedly. But, in reality, there is no way to express my gratitude for the spirit of generosity impressed upon me at such an early age and the demonstration of how important family and friends are. These are two lessons that my parents did not just tell me. They showed me with their lives, and these teachings have been the basis of my life.
        It was in this simple house that my parents welcomed other refugees to celebrate their arrival to this country and where I celebrated my first birthdays. It was in the warmth of the kitchen in this humble house where a Cuban feast (albeit a frugal Cuban feast) always filled the air with not just scent and music but life and love. It was here where I learned the real definition of “family.” And for this, I will never forget that house or its gracious neighborhood or the many things I learned there about how to love. I will never forget how my parents turned this simple house into a home.
        `
        Prompt:`
        Describe the mood created by the author in the memoir. Support your answer with relevant and specific information from the memoir.
        `
        """
        self.Set_2_Rubric = """
        Scoring Guide:`
        Score Point 4: The response is a clear, complete, and accurate description of the mood created by the author. The response includes relevant and specific information from the memoir.    
        Score Point 3: The response is a mostly clear, complete, and accurate description of the mood created by the author. The response includes relevant but often general information from the memoir.
        Score Point 2: The response is a partial description of the mood created by the author. The response includes limited information from the memoir and may include misinterpretations.
        Score Point 1: The response is a minimal description of the mood created by the author. The response includes little or no information from the memoir and may include misinterpretations. OR The response relates minimally to the task.
        Score Point 0: The response is incorrect or irrelevant or contains insufficient information to demonstrate comprehension.
        `

        Scoring Notes:`
        The response should describe a mood of gratitude, love, or any similar appreciative mood. The response may include, but is not limited to: 
        - in paragraph 2: the author says he is “eternally grateful” to his parents for instilling in him a love of cooking. He also credits them for his appreciation of Cuban music “which I adore to this day.” In general he notes their having made an inviting home 
        filled with “endless celebrations” out of “modest” means. 
        - in paragraph 3: the author credits his parents for instilling in him a great sense of “family” due to the “environment” they created. This sense of family extended to everyone in a time when the larger world was uninviting. 
        - in paragraph 4: the author mentions his family's generosity in allowing others to stay with them and notes its reciprocal nature 
        - in paragraph 5: the author recognizes that his parents came to America “selflessly” in order to “give their children a better life.” He details their challenges and obstacles and observes that they “endured.” 
        - in paragraph 6: the author states, “I will always be grateful to my parents for their love and sacrifice. I've often told them that what they did was a much more courageous thing than I could have ever done.” He mentions his admiration and having thanked them yet admits that he has, “no way to express my gratitude.” 
        - in paragraph 7: the author states, “I will never forget that house or its gracious neighborhood or the many things I learned there about how to love. I will never forget how my parents turned this simple house into a home.” 
        In conclusion, the author creates an appreciative mood by describing all of the things he is grateful for including his parents and the home they made for him. 
        Other interpretations are acceptable if supported by relevant evidence from the text.`
        """
        self.Set_2_Task_Decomposition = """
        1. **Review Materials:**
        - **Read Prompt and Rubric:** Understand the essay prompt and thoroughly review the scoring guide and scoring notes to identify key points for each score level.
        - **Read Student's Essay:** Comprehend the student's response to the prompt.
        2. **Identify and Extract Key Points:**
        - **List Key Elements:** From the scoring notes, enumerate specific situations, themes, or elements (e.g., expressions of gratitude, family dynamics, cultural solidarity, parental sacrifices).
        - **Locate in Essay:** Find and highlight sections in the student's essay that correspond to each key point.
        3. **Evaluate Key Points:**
        - **Assess Coverage:** Determine if each key point is adequately addressed, noting the depth of exploration and supporting evidence.
        - **Match to Rubric:** Align the presence and thoroughness of each key point with the rubric's scoring criteria.
        4. **Structure Evaluation:**
        - **Provide Explanations and Evidences:**
            - **Explanations:** For each key point, clearly explain how the essay addresses or fails to address it based on rubric expectations.
            - **Evidences:** Cite direct quotes or specific references from the essay to support each explanation.
        - **Organize Logically:** Present explanations and evidences in a coherent sequence covering all relevant key points.
        5. **Assign and Present Scores:**
        - **Score Assignment:** Based on the evaluation, assign scores according to the rubric, considering both the rubric guidelines and the identified key points.
        - **Final Evaluation Format:** Conclude with the final evaluation strictly formatted as:
            ```
            Your final evaluation:
            [Final Score: ...]
            ```
        6. **Ensure Integrity and Quality:**
        - **Maintain Anonymization:** Handle any anonymized information consistently without altering meaning, focusing solely on content quality.
        - **Quality Assurance:** Review the evaluation for completeness, accuracy of evidences, and alignment with the rubric to ensure clarity and objectivity.
        """
        ###

        # Source, Prompt, Rubric and Task Decomposition for Dataset 3
        self.Set_3_Prompt = """
        We all understand the benefits of laughter. For example, someone once said, “Laughter is the shortest distance between two people.” Many other people believe that laughter is an important part of any relationship. Tell a true story in which laughter was one element or part.
        """
        self.Set_3_Rubric = """
        \n A rating of 1-6 on the following six traits:

        \n Ideas and Content:
        \n Score 6: The writing is exceptionally clear, focused, and interesting. It holds the reader's attention throughout. Main ideas stand out and are developed by strong support and rich details suitable to audience and purpose. The writing is characterized by
        •	clarity, focus, and control.
        •	main idea(s) that stand out.
        •	supporting, relevant, carefully selected details; when appropriate, use of resources provides strong, accurate, credible support.
        •	a thorough, balanced, in-depth explanation / exploration of the topic; the writing makes connections and shares insights.
        •	content and selected details that are well-suited to audience and purpose.

        \n Score 5: The writing is clear, focused and interesting. It holds the reader's attention. Main ideas stand out and are developed by supporting details suitable to audience and purpose. The writing is characterized by
        •	clarity, focus, and control.
        •	main idea(s) that stand out.
        •	supporting, relevant, carefully selected details; when appropriate, use of resources provides strong, accurate, credible support.
        •	a thorough, balanced explanation / exploration of the topic; the writing makes connections and shares insights.
        •	content and selected details that are well-suited to audience and purpose.

        \n Score 4: The writing is clear and focused. The reader can easily understand the main ideas. Support is present, although it may be limited or rather general. The writing is characterized by
        •	an easily identifiable purpose.
        •	clear main idea(s).
        •	supporting details that are relevant, but may be overly general or limited in places; when appropriate, resources are used to provide accurate support.
        •	a topic that is explored / explained, although developmental details may occasionally be out of balance with the main idea(s); some connections and insights may be present.
        •	content and selected details that are relevant, but perhaps not consistently well-chosen for audience and purpose.

        \n Score 3: The reader can understand the main ideas, although they may be overly broad or simplistic, and the results may not be effective. Supporting detail is often limited, insubstantial, overly general, or occasionally slightly off-topic. The writing is characterized by
        •	an easily identifiable purpose and main idea(s).
        •	predictable or overly-obvious main ideas; or points that echo observations heard elsewhere; or a close retelling of another work.
        •	support that is attempted, but developmental details are often limited, uneven, somewhat off-topic, predictable, or too general (e.g., a list of underdeveloped points).
        •	details that may not be well-grounded in credible resources; they may be based on clichés, stereotypes or questionable sources of information.
        •	difficulties when moving from general observations to specifics.

        \n Score 2: Main ideas and purpose are somewhat unclear or development is attempted but minimal. The writing is characterized by
        •	a purpose and main idea(s) that may require extensive inferences by the reader.
        •	minimal development; insufficient details.
        •	irrelevant details that clutter the text.
        •	extensive repetition of detail.

        \n Score 1: The writing lacks a central idea or purpose. The writing is characterized by
        •	ideas that are extremely limited or simply unclear.
        •	attempts at development that are minimal or nonexistent; the paper is too short to demonstrate the development of an idea.

        \n Organization:
        \n Score 6: The organization enhances the central idea(s) and its development. The order and structure are compelling and move the reader through the text easily. The writing is characterized by
        •	effective, perhaps creative, sequencing and paragraph breaks; the organizational structure fits the topic, and the writing is easy to follow.
        •	a strong, inviting beginning that draws the reader in and a strong, satisfying sense of resolution or closure.
        •	smooth, effective transitions among all elements (sentences, paragraphs, ideas).
        •	details that fit where placed.

        \n Score 5: The organization enhances the central idea(s) and its development. The order and structure are strong and move the reader through the text. The writing is characterized by
        •	effective sequencing and paragraph breaks; the organizational structure fits the topic, and the writing is easy to follow.
        •	an inviting beginning that draws the reader in and a satisfying sense of resolution or closure.
        •	smooth, effective transitions among all elements (sentences, paragraphs, ideas).
        •	details that fit where placed.

        \n Score 4: Organization is clear and coherent. Order and structure are present, but may seem formulaic. The writing is characterized by
        •	clear sequencing and paragraph breaks.
        •	an organization that may be predictable.
        •	a recognizable, developed beginning that may not be particularly inviting; a developed conclusion that may lack subtlety.
        •	a body that is easy to follow with details that fit where placed.
        •	transitions that may be stilted or formulaic.
        •	organization which helps the reader, despite some weaknesses.

        \n Score 3: An attempt has been made to organize the writing; however, the overall structure is inconsistent or skeletal. The writing is characterized by
        •	attempts at sequencing and paragraph breaks, but the order or the relationship among ideas may occasionally be unclear.
        •	a beginning and an ending which, although present, are either undeveloped or too obvious (e.g., “My topic is...”; “These are all the reasons that...”).
        •	transitions that sometimes work. The same few transitional devices (e.g., coordinating conjunctions, numbering, etc.) may be overused.
        •	a structure that is skeletal or too rigid.
        •	placement of details that may not always be effective.
        •	organization which lapses in some places, but helps the reader in others.

        \n Score 2: The writing lacks a clear organizational structure. An occasional organizational device is discernible; however, the writing is either difficult to follow and the reader has to reread substantial portions, or the piece is simply too short to demonstrate organizational skills. The writing is characterized by
        •	some attempts at sequencing, but the order or the relationship among ideas is frequently unclear; a lack of paragraph breaks.
        •	a missing or extremely undeveloped beginning, body, and/or ending.
        •	a lack of transitions, or when present, ineffective or overused.
        •	a lack of an effective organizational structure.
        •	details that seem to be randomly placed, leaving the reader frequently confused.

        \n Score 1: The writing lacks coherence; organization seems haphazard and disjointed. Even after rereading, the reader remains confused. The writing is characterized by
        •	a lack of effective sequencing and paragraph breaks.
        •	a failure to provide an identifiable beginning, body and/or ending.
        •	a lack of transitions.
        •	pacing that is consistently awkward; the reader feels either mired down in trivia or rushed along too rapidly.
        •	a lack of organization which ultimately obscures or distorts the main point.

        \n Voice:
        \n Score 6: The writer has chosen a voice appropriate for the topic, purpose, and audience. The writer demonstrates deep commitment to the topic, and there is an exceptional sense of “writing to be read.” The writing is expressive, engaging, or sincere. The writing is characterized by
        •	an effective level of closeness to or distance from the audience (e.g., a narrative should have a strong personal voice, while an expository piece may require extensive use of outside resources and a more academic voice; nevertheless, both should be engaging, lively, or interesting. Technical writing may require greater distance.).
        •	an exceptionally strong sense of audience; the writer seems to be aware of the reader and of how to communicate the message most effectively. The reader may discern the writer behind the words and feel a sense of interaction.
        •	a sense that the topic has come to life; when appropriate, the writing may show originality, liveliness, honesty, conviction, excitement, humor, or suspense.

        \n Score 5: The writer has chosen a voice appropriate for the topic, purpose, and audience. The writer demonstrates commitment to the topic, and there is a sense of “writing to be read.” The writing is expressive, engaging, or sincere. The writing is characterized by an appropriate level of closeness to or distance from the audience (e.g., a narrative should have a strong personal voice, while an expository piece may require extensive use of outside resources and a more academic voice; nevertheless, both should be engaging, lively, or interesting. Technical writing may require greater distance.).
        •	a strong sense of audience; the writer seems to be aware of the reader and of how to communicate the message most effectively. The reader may discern the writer behind the words and feel a sense of interaction.
        •	a sense that the topic has come to life; when appropriate, the writing may show originality, liveliness, honesty, conviction, excitement, humor, or suspense.

        \n Score 4: A voice is present. The writer seems committed to the topic, and there may be a sense of “writing to be read.” In places, the writing is expressive, engaging, or sincere. The writing is characterized by
        •	a suitable level of closeness to or distance from the audience.
        •	a sense of audience; the writer seems to be aware of the reader but has not consistently employed an appropriate voice. The reader may glimpse the writer behind the words and feel a sense of interaction in places.
        •	liveliness, sincerity, or humor when appropriate; however, at times the writing may be either inappropriately casual or personal, or inappropriately formal and stiff.

        \n Score 3: The writer's commitment to the topic seems inconsistent. A sense of the writer may emerge at times; however, the voice is either inappropriately personal or inappropriately impersonal. The writing is characterized by
        •	a limited sense of audience; the writer's awareness of the reader is unclear.
        •	an occasional sense of the writer behind the words; however, the voice may shift or disappear a line or two later and the writing become somewhat mechanical.
        •	a limited ability to shift to a more objective voice when necessary.
        •	text that is too short to demonstrate a consistent and appropriate voice.

        \n Score 2: The writing provides little sense of involvement or commitment. There is no evidence that the writer has chosen a suitable voice. The writing is characterized by
        •	little engagement of the writer; the writing tends to be largely flat, lifeless, stiff, or mechanical.
        •	a voice that is likely to be overly informal and personal.
        •	a lack of audience awareness; there is little sense of “writing to be read.”
        •	little or no hint of the writer behind the words. There is rarely a sense of interaction between reader and writer.

        \n Score 1: The writing seems to lack a sense of involvement or commitment. The writing is characterized by
        •	no engagement of the writer; the writing is flat and lifeless.
        •	a lack of audience awareness; there is no sense of “writing to be read.”
        •	no hint of the writer behind the words. There is no sense of interaction between writer and reader; the writing does not involve or engage the reader.

        \n Word Choice:
        \n Score 6: Words convey the intended message in an exceptionally interesting, precise, and natural way appropriate to audience and purpose. The writer employs a rich, broad range of words which have been carefully chosen and thoughtfully placed for impact. The writing is characterized by
        •	accurate, strong, specific words; powerful words energize the writing.
        •	fresh, original expression; slang, if used, seems purposeful and is effective.
        •	vocabulary that is striking and varied, but that is natural and not overdone.
        •	ordinary words used in an unusual way.
        •	words that evoke strong images; figurative language may be used.

        \n Score 5: Words convey the intended message in an interesting, precise, and natural way appropriate to audience and purpose. The writer employs a broad range of words which have been carefully chosen and thoughtfully placed for impact. The writing is characterized by
        •	accurate, specific words; word choices energize the writing.
        •	fresh, vivid expression; slang, if used, seems purposeful and is effective.
        •	vocabulary that may be striking and varied, but that is natural and not overdone.
        •	ordinary words used in an unusual way.
        •	words that evoke clear images; figurative language may be used.

        \n Score 4: Words effectively convey the intended message. The writer employs a variety of words that are functional and appropriate to audience and purpose. The writing is characterized by
        •	words that work but do not particularly energize the writing.
        •	expression that is functional; however, slang, if used, does not seem purposeful and is not particularly effective.
        •	attempts at colorful language that may occasionally seem overdone.
        •	occasional overuse of technical language or jargon.
        •	rare experiments with language; however, the writing may have some fine moments and generally avoids clichés.

        \n Score 3: Language lacks precision and variety, or may be inappropriate to audience and purpose in places. The writer does not employ a variety of words, producing a sort of “generic” paper filled with familiar words and phrases. The writing is characterized by
        •	words that work, but that rarely capture the reader’s interest.
        •	expression that seems mundane and general; slang, if used, does not seem purposeful and is not effective.
        •	attempts at colorful language that seem overdone or forced.
        •	words that are accurate for the most part, although misused words may occasionally appear; technical language or jargon may be overused or inappropriately used.
        •	reliance on clichés and overused expressions.
        •	text that is too short to demonstrate variety.

        \n Score 2: Language is monotonous and/or misused, detracting from the meaning and impact. The writing is characterized by
        •	words that are colorless, flat or imprecise.
        •	monotonous repetition or overwhelming reliance on worn expressions that repeatedly detract from the message.
        •	images that are fuzzy or absent altogether.

        \n Score 1: The writing shows an extremely limited vocabulary or is so filled with misuses of words that the meaning is obscured. Only the most general kind of message is communicated because of vague or imprecise language. The writing is characterized by
        •	general, vague words that fail to communicate.
        •	an extremely limited range of words.
        •	words that simply do not fit the text; they seem imprecise, inadequate, or just plain wrong.

        \n Sentence Fluency:
        \n Score 6: The writing has an effective flow and rhythm. Sentences show a high degree of craftsmanship, with consistently strong and varied structure that makes expressive oral reading easy and enjoyable. The writing is characterized by
        •	a natural, fluent sound; it glides along with one sentence flowing effortlessly into the next.
        •	extensive variation in sentence structure, length, and beginnings that add interest to the text.
        •	sentence structure that enhances meaning by drawing attention to key ideas or reinforcing relationships among ideas.
        •	varied sentence patterns that create an effective combination of power and grace.
        •	strong control over sentence structure; fragments, if used at all, work well.
        •	stylistic control; dialogue, if used, sounds natural.

        \n Score 5: The writing has an easy flow and rhythm. Sentences are carefully crafted, with strong and varied structure that makes expressive oral reading easy and enjoyable. The writing is characterized by
        •	a natural, fluent sound; it glides along with one sentence flowing into the next.
        •	variation in sentence structure, length, and beginnings that add interest to the text.
        •	sentence structure that enhances meaning.
        •	control over sentence structure; fragments, if used at all, work well.
        •	stylistic control; dialogue, if used, sounds natural.

        \n Score 4: The writing flows; however, connections between phrases or sentences may be less than fluid. Sentence patterns are somewhat varied, contributing to ease in oral reading. The writing is characterized by
        •	a natural sound; the reader can move easily through the piece, although it may lack a certain rhythm and grace.
        •	some repeated patterns of sentence structure, length, and beginnings that may detract somewhat from overall impact.
        •	strong control over simple sentence structures, but variable control over more complex sentences; fragments, if present, are usually effective.
        •	occasional lapses in stylistic control; dialogue, if used, sounds natural for the most part, but may at times sound stilted or unnatural.

        \n Score 3: The writing tends to be mechanical rather than fluid. Occasional awkward constructions may force the reader to slow down or reread. The writing is characterized by
        •	some passages that invite fluid oral reading; however, others do not.
        •	some variety in sentence structure, length, and beginnings, although the writer falls into repetitive sentence patterns.
        •	good control over simple sentence structures, but little control over more complex sentences; fragments, if present, may not be effective.
        •	sentences which, although functional, lack energy.
        •	lapses in stylistic control; dialogue, if used, may sound stilted or unnatural.
        •	text that is too short to demonstrate variety and control.

        \n Score 2: The writing tends to be either choppy or rambling. Awkward constructions often force the reader to slow down or reread. The writing is characterized by
        •	significant portions of the text that are difficult to follow or read aloud.
        •	sentence patterns that are monotonous (e.g., subject-verb or subject-verb-object).
        •	a significant number of awkward, choppy, or rambling constructions.

        \n Score 1: The writing is difficult to follow or to read aloud. Sentences tend to be incomplete, rambling, or very awkward. The writing is characterized by
        •	text that does not invite—and may not even permit—smooth oral reading.
        •	confusing word order that is often jarring and irregular.
        •	sentence structure that frequently obscures meaning.
        •	sentences that are disjointed, confusing, or rambling.

        \n Conventions:
        \n Score 6: The writing demonstrates exceptionally strong control of standard writing conventions (e.g., punctuation, spelling, capitalization, grammar and usage) and uses them effectively to enhance communication. Errors are so few and so minor that the reader can easily skim right over them unless specifically searching for them. The writing is characterized by
        •	strong control of conventions; manipulation of conventions may occur for stylistic effect.
        •	strong, effective use of punctuation that guides the reader through the text.
        •	correct spelling, even of more difficult words.
        •	correct grammar and usage that contribute to clarity and style.
        •	skill in using a wide range of conventions in a sufficiently long and complex piece.
        •	little or no need for editing.

        \n Score 5: The writing demonstrates strong control of standard writing conventions (e.g., punctuation, spelling, capitalization, grammar and usage) and uses them effectively to enhance communication. Errors are few and minor. Conventions support readability. The writing is characterized by
        •	strong control of conventions.
        •	effective use of punctuation that guides the reader through the text.
        •	correct spelling, even of more difficult words.
        •	correct capitalization; errors, if any, are minor.
        •	correct grammar and usage that contribute to clarity and style.
        •	skill in using a wide range of conventions in a sufficiently long and complex piece.
        •	little need for editing.

        \n Score 4: The writing demonstrates control of standard writing conventions (e.g., punctuation, spelling, capitalization, grammar and usage). Significant errors do not occur frequently. Minor errors, while perhaps noticeable, do not impede readability. The writing is characterized by
        •	control over conventions used, although a wide range is not demonstrated.
        •	correct end-of-sentence punctuation; internal punctuation may sometimes be incorrect.
        •	spelling that is usually correct, especially on common words.
        •	correct capitalization; errors, if any, are minor.
        •	occasional lapses in correct grammar and usage; problems are not severe enough to distort meaning or confuse the reader.
        •	moderate need for editing.

        \n Score 3: The writing demonstrates limited control of standard writing conventions (e.g., punctuation, spelling, capitalization, grammar and usage). Errors begin to impede readability. The writing is characterized by
        •	some control over basic conventions; the text may be too simple or too short to reveal mastery.
        •	end-of-sentence punctuation that is usually correct; however, internal punctuation contains frequent errors.
        •	spelling errors that distract the reader; misspelling of common words occurs.
        •	capitalization errors.
        •	errors in grammar and usage that do not block meaning but do distract the reader.
        •	significant need for editing.

        \n Score 2: The writing demonstrates little control of standard writing conventions. Frequent, significant errors impede readability. The writing is characterized by
        •	little control over basic conventions.
        •	many end-of-sentence punctuation errors; internal punctuation contains frequent errors.
        •	spelling errors that frequently distract the reader; misspelling of common words often occurs.
        •	capitalization that is inconsistent or often incorrect.
        •	errors in grammar and usage that interfere with readability and meaning.
        •	substantial need for editing.

        \n  Score 1: Numerous errors in usage, spelling, capitalization, and punctuation repeatedly distract the reader and make the text difficult to read. In fact, the severity and frequency of errors are so overwhelming that the reader finds it difficult to focus on the message and must reread for meaning. The writing is characterized by
        •	very limited skill in using conventions.
        •	basic punctuation (including end-of-sentence punctuation) that tends to be omitted, haphazard, or incorrect.
        •	frequent spelling errors that significantly impair readability.
        •	capitalization that appears to be random.
        •	a need for extensive editing.
        """
        self.Set_3_Examples = """

        """
        self.Set_3_Task_Decomposition = """
        \n 1. Carefully read the provided essay prompt, scoring guidelines, and the student's essay.
        \n 2. In the Explanations part, identify elements referring to the rubrics, then provide the specific evidences in the student's essay to supprot the elements. The Explanations for each dimension should be as detailed as possible.
        \n 3. Determine the appropriate scores according to the analysis above, and then calculate the Final socre. You Should score every dimension.
           Final Score = Ideas and Content Score + Organization Score + Sentence Fluency Score + Conventions Score * 2  
           For example, `[Ideas and Content Score: 1, Organization Score: 2, Voice Score: 3, Word Choice Score: 4, Sentence Fluency Score: 5, Conventions Score: 6] => Final Score = 1 + 2 + 5 + 6 * 2 = 20 => [Final Score: 20]`
        \n Please STRICTLY present your evaluation in the following manner:`
        \n Explanations: ..., Ideas and Content Score: ...
        \n Explanations: ..., Organization Score: ...
        \n Explanations: ..., Voice Score: ...
        \n Explanations: ..., Word Choice Score: ...
        \n Explanations: ..., Sentence Fluency Score: ...
        \n Explanations: ..., Conventions Score: ...
        \n Your final evaluation:
        \n [Ideas and Content Score: ..., Organization Score: ..., Voice Score: ..., Word Choice Score: ..., Sentence Fluency Score: ..., Conventions Score: ...]
        \n [Final Score: ...]`
        """
        ###