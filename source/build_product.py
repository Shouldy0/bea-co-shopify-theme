from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import Paragraph, Frame, Image, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader, PdfWriter
import json
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'output/pdf'; OUT.mkdir(parents=True,exist_ok=True)
W,H=595.28,841.89
ink=HexColor('#263832'); muted=HexColor('#56645c'); cream=HexColor('#F7F3EC'); gold=HexColor('#A86A3D'); sage=HexColor('#E5EBDF')
body=ParagraphStyle('Body',fontName='Helvetica',fontSize=11.3,leading=17.2,textColor=ink,spaceAfter=12)
small=ParagraphStyle('Small',parent=body,fontSize=9.4,leading=14)
head=ParagraphStyle('Head',parent=body,fontName='Helvetica-Bold',fontSize=13,leading=18,spaceBefore=9,spaceAfter=8)
photo=ROOT/'output/brand/bea-original.jpg'
pages=[]
def add(title,kicker,blocks): pages.append(dict(title=title,kicker=kicker,blocks=blocks))
add('Start here','01 / A KINDER START',[
('p','This guide is a practical companion for noticing what happens around alone time, organising small steps and keeping useful records. It is an owner-created educational resource, not an individual treatment plan. Use it alongside professional advice when your dog finds separation difficult.'),
('h','Meet Bea'),('p','Bea is the dog behind Bea &amp; Co. Her photo belongs here because this project starts with a real dog and the person who cares for her. This guide does not claim that every dog will follow the same path, or promise a particular outcome.'),
('h','How to use the kit'),('p','Read the guide before attempting exercises. Open the separate workbook and save a copy with your dog\'s name. Complete the starting-point page, keep one session record at a time, then review patterns with your support professional. Print fresh pages whenever you need them.'),
('h','When this guide is not enough'),('p','Arrange a veterinary assessment for suspected separation-related distress, especially with new symptoms or toileting changes. Injury, frantic escape attempts or severe distress need prompt professional help. Do not run an absence test to prove that a dog is struggling. Medication decisions belong with your veterinarian. [1]'),
('p','No fixed recovery time is promised. A quiet dog is not automatically a comfortable dog. The aim is to understand the individual in front of you, not to reach a number on a calendar.')])
add('Your quick-start map','02 / READ BEFORE PRACTISING',[
('h','1. Understand the starting point'),('p','Write down what you already know: what happens before departures, which situations are easier, and whether someone can remain with your dog. Existing video may be useful; you do not need to provoke distress to gather evidence.'),
('h','2. Make daily life manageable'),('p','List realistic cover for necessary absences. A trusted person staying with your dog may help, but confirm that your dog is comfortable with that arrangement. A walk halfway through a long absence does not provide company during the time before and after it.'),
('h','3. Choose an achievable action'),('p','An action can be as small as approaching a door while remaining in view. Start with something your dog already handles comfortably. If even that is difficult, work with a qualified professional rather than improvising increasingly stressful tests.'),
('h','4. Observe, return, record'),('p','Watch the whole dog. Return promptly if distress appears; do not wait for silence as a condition of returning. Record the exact action and what you saw. Give your dog time to settle, and stop if you are unsure.'),
('h','5. Review before changing anything'),('p','Use observations across sessions to inform the next choice. A good day is useful information, not permission for a large jump. Your professional can help translate the records into an individual plan.'),
('p','Keep the one-page Quick Reference nearby. It is a reminder of the guide, not a shortcut around reading it.')])
add('Understand the behaviour','03 / CONTEXT COMES FIRST',[
('p','Barking, damage or toileting during an absence can have different explanations. The label "separation anxiety" should not be inferred from a damaged door or a neighbour\'s report alone. This guide uses "separation-related distress" descriptively, without diagnosing your dog.'),
('h','Look for a pattern'),('p','Record when the behaviour begins, what was happening just before it, whether the dog was alone, and whether noises or confinement may have played a part. Write observations such as "walked between the door and window" instead of conclusions such as "was angry with me".'),
('h','What this changes'),('p','Treat difficulty as information. Punishment is not an appropriate response to separation-related distress. Video can help you see patterns that are otherwise hidden when you return home. Consult your veterinarian if symptoms persist or their cause is unclear. [2]'),
('h','Keep the goal realistic'),('p','A useful goal describes a situation your household needs to manage and the support available while you work toward it. "Arrange comfortable cover for Tuesday morning" may be more useful today than "reach two hours by Friday".'),
('h','A note for the human'),('p','You do not need perfect records or a perfect routine to begin organising support. Use short, factual notes. If the process is overwhelming, reduce the administrative burden and ask for help. The workbook is meant to make decisions easier.')])
add('Read the whole dog','04 / OBSERVATION',[
('p','Compare behaviour with your dog\'s usual relaxed state. Record posture, movement, breathing, sounds and ability to settle together. A single yawn, a refused snack or one bark does not establish a diagnosis.'),
('h','Possible observations to record'),('p','Repeated pacing; sustained vocalising; trembling; drooling; panting without an obvious explanation; repeated checking of an exit; tense stillness; attempts to escape; or a change in eating. Note the circumstances instead of assigning meaning automatically.'),
('h','Use precise words'),('p','"Whale eye" describes visible eye white; it is not the same as a dilated pupil. Write down what you can actually see. If the camera angle is poor, mark the observation as uncertain rather than assuming your dog was calm.'),
('h','Quiet is not the only goal'),('p','A dog can be silent while remaining tense. Likewise, eating does not prove that the whole absence was comfortable. Observe the period before, during and after any activity, including what happens when a food toy is finished.'),
('h','A simple recording key'),('p','<b>Comfortable:</b> behaviour looks like the dog\'s relaxed baseline.<br/><b>Uncertain:</b> you cannot confidently interpret the behaviour or see the dog.<br/><b>Distress:</b> concerning changes, escalation or clear difficulty are present.'),
('p','This key is an organisational tool, not a validated clinical scale. Uncertain is a reason to pause and review, not a green light to make the exercise harder.')])
add('Prepare the environment','05 / BEFORE THE DOOR',[
('h','Choose familiar comfort'),('p','Use a space your dog already finds comfortable. Check access to water, temperature, resting places and household hazards. Closing a gate or crate can change the situation, so do not assume a smaller space will be easier.'),
('h','Observe without leaving the dog unsupported'),('p','For live exercises, use a live camera or video call with a reliable view and sound, and stay close enough to return immediately. A recording you can only watch later is useful for review, but cannot alert you to distress during practice.'),
('h','Keep tools optional'),('p','A notebook and a way to observe may be enough. No particular camera, diffuser or toy is required by this guide. If you use enrichment, choose something appropriate for your dog and already assessed for safe use. Food is not a substitute for a suitable absence plan.'),
('h','Make the comparison fair'),('p','Record factors that could affect a session: visitors, unusual noise, poor sleep, a change of room or who is home. Do not change several elements at once and then assume duration alone explains the result.'),
('h','Before starting'),('p','Check: the dog is settled; you can observe; you know the planned action; you can return at once; and you have time to record what happened. If one of these is missing, choose an observation or planning task instead.')])
add('Plan for ordinary life','06 / YOUR SUPPORT PLAN',[
('p','Training and unavoidable real-world absences are different problems. A workable plan accounts for both. Use the support page to identify when company is needed and who can provide it.'),
('h','Match support to the dog'),('p','A familiar sitter at home, a trusted friend or another arrangement may work. Check the dog\'s comfort with the person and place before relying on it. Daycare or another dog is not automatically the right fit.'),
('h','Plan the entire absence'),('p','Write departure and return times, travel margins and a backup contact. Clarify whether the helper will remain throughout the absence. Record what should happen if plans change or the dog becomes distressed.'),
('h','If an unavoidable absence happens'),('p','Use the safest feasible arrangement and seek help with ongoing gaps. Record the event separately from planned practice. Do not treat a difficult real-world absence as a training success because it lasted longer.'),
('h','Return to observation'),('p','After a disruption, assess the dog\'s current comfort instead of trying to recover lost minutes. A previous record remains useful history, but it is not a guarantee of what the dog can manage today.'),
('p','Support is part of the plan. Asking for company, adjusting a schedule or consulting a professional is a practical response to the problem, not a failure of commitment.')])
add('Find a comfortable start','07 / NO STRESS TEST',[
('p','The original guide called this finding the threshold. Here, think of a comfortable starting point: a known action that does not visibly concern your dog. You do not need to discover the longest possible absence.'),
('h','Use existing information first'),('p','Note an action your dog already tolerates, such as you shifting in your chair or moving toward a doorway. Closing the front door is not a universal first step. Some dogs need support before any out-of-sight practice is appropriate.'),
('h','Record one clear action'),('p','Include the location, who was home, what you did and what the dog did. For example: "Stood beside the hallway door; stayed visible; dog remained resting." This is an example of notation, not an instruction that every dog should repeat it.'),
('h','If uncertainty appears'),('p','Stop the exercise, rejoin your dog and review the observation. Do not repeat the action until the dog appears fully settled simply to obtain a better-looking record. Discuss ambiguous signals with your professional.'),
('h','Before you progress'),('p','You should be able to describe what comfortable behaviour looked like and why the next action is appropriate. If you cannot, the next task is more observation or professional guidance, not a longer absence.'),
('p','Keep your starting-point record dated. It is a snapshot of a particular situation, not a permanent score for your dog.')])
add('Departure cues, gently','08 / AN INDIVIDUAL STEP',[
('p','Keys, shoes or a bag may become noticeable parts of leaving. Observe whether those cues actually concern your dog. A dog who is comfortable with keys does not need a mandatory week of key exercises.'),
('h','Keep the action small'),('p','If your professional recommends cue practice, begin with a manageable version and change one element at a time. Do not repeatedly jingle keys at an already worried dog to make the reaction disappear.'),
('h','Avoid rigid repetition targets'),('p','There is no prescribed number of repetitions in this workbook. Write down what happened and allow recovery between activities. A stressed dog does not need extra repetitions to finish a quota.'),
('h','Combine only when appropriate'),('p','Several individually easy actions may become harder when combined. Putting on shoes, lifting a bag and touching a handle is a different event from any one of those actions alone. Record the combination explicitly.'),
('h','What to write'),('p','Cue or action; context; response; recovery; and the proposed next step. Keep plans separate from observations so you can tell what was intended and what actually happened.'),
('p','Progress is not measured by whether the dog ignores you completely. Look for comfort in context, and have a qualified professional help if you are unsure how to interpret the response.')])
add('Organise a short session','09 / PLAN, OBSERVE, RECORD',[
('h','Before'),('p','Read the previous record. Choose an action within current comfort and write it down. Confirm that live observation and a prompt return are possible. Decide in advance to stop if the dog becomes unsettled or you lose the camera view.'),
('h','During'),('p','Perform the planned action while observing the dog. Do not extend it spontaneously because things seem to be going well. If distress appears, return promptly and calmly; do not require quiet before returning.'),
('h','After'),('p','Allow the dog to settle. Record the actual duration and unit, or write "no absence" for an in-view action. Describe the response, not just whether you consider it a success. Do not start another departure while the dog remains unsettled.'),
('h','Decide what comes next'),('p','Comfortable: record it and review the overall pattern before changing difficulty.<br/>Uncertain: pause and review the video or ask for help.<br/>Distress: stop, return to an easier plan and seek support if needed.'),
('h','Make greetings natural'),('p','Keep your manner calm and reassuring. This guide does not require you to withhold affection or ignore your dog. The useful question is whether the routine supports comfort, not whether you performed an exact greeting ritual.'),
('p','Session frequency, progression and rest should suit the individual dog. More departures are not automatically better.')])
add('Progress without a deadline','10 / COMFORT BEFORE DURATION',[
('p','Avoid fixed weekly targets and automatic jumps from seconds to minutes or from minutes to hours. The workbook does not prescribe a universal timetable. Agree individual progression with the professional supporting you.'),
('h','Change one thing you can describe'),('p','Duration, the door used, time of day, departure cues and who is home can all change the experience. Record the change. A comfortable practice in one setting does not demonstrate comfort in every setting.'),
('h','Measure the pattern'),('p','Look at several records together. Was the dog comfortable throughout? Was recovery easy? Was the camera view adequate? Did a longer duration coincide with uncertainty? The largest number is not necessarily the most useful result.'),
('h','Keep units explicit'),('p','Write 3 seconds, not just 3. Use seconds for micro-absences and minutes only when appropriate. Avoid rounding an absence upward or treating planned time as actual time.'),
('h','No milestone guarantees'),('p','Reaching a particular duration does not guarantee readiness for a much longer absence. Plan real-life needs separately, including appropriate care, company and breaks for the dog.'),
('p','A sensible review can conclude "repeat an easier action" or "ask for advice". The record should help you make that decision, not pressure you to produce a rising graph.')])
add('When things get difficult','11 / TROUBLESHOOTING',[
('h','The dog seemed comfortable yesterday'),('p','Record what changed and reassess today. Do not insist on yesterday\'s duration. New or persistent changes warrant a veterinary discussion, especially if the dog seems unwell.'),
('h','The dog will not eat'),('p','Note when it happened, what was offered and other behaviour. Refusing food is not a stand-alone diagnosis; eating is not proof of comfort either. Do not increase food value to justify an otherwise difficult absence.'),
('h','The camera failed'),('p','End the exercise and restore observation before trying again. Mark the record as uncertain rather than assuming the unseen period went well.'),
('h','I do not have enough time'),('p','Prioritise support arrangements and a manageable record. Ask your professional to help design a feasible schedule. Do not squeeze repeated departures into a short break at the expense of the dog\'s recovery.'),
('h','The dog is vocalising or trying to escape'),('p','Return promptly, make the situation safe and stop the exercise. Seek prompt veterinary help for injury or severe distress. Do not wait outside for the dog to stop as a training rule.'),
('h','I cannot tell whether this is working'),('p','Bring a few representative records and videos to a qualified professional. Include uncertainty and setbacks; those entries can be more informative than the best-looking session.')])
add('Review and maintain','12 / A USEFUL WEEKLY CHECK-IN',[
('h','Review the week, not a streak'),('p','Use the weekly page to record comfortable situations, concerning changes, support that worked and questions for your next appointment. Leave gaps when no exercise happened. There is no streak to protect.'),
('h','Keep maintenance individual'),('p','Continue observing your dog when routines change. Moving house, different work hours or a new caregiver may require a fresh plan. Do not assume past performance automatically transfers to a new setting.'),
('h','Know what your records cannot prove'),('p','A session log is your observation, not a diagnosis, controlled study or guarantee. Be honest about missing footage, distractions and unknowns. Your notes can support a professional conversation without replacing one.'),
('h','Make the kit work for you'),('p','Duplicate only the pages you use. You may prefer a paper log, a saved PDF or short notes transferred later. Store videos separately with filenames that match the date and session record. Avoid collecting more detail than you can maintain.'),
('h','The practical goal'),('p','A clearer picture of your dog, a more workable support plan and records that make the next conversation easier. Let those be the measures of this workbook\'s usefulness.'),
('p','Bea &amp; Co. / Small steps. Thoughtful care.')])
add('An example, not a target','13 / HOW TO COMPLETE A RECORD',[
('p','The following record is fictional and illustrates how to write observations. It is not Bea\'s history, a testimonial or a recommended exercise sequence.'),
('h','A clearly recorded session'),('p','<b>Context:</b> Tuesday, quiet afternoon; caregiver at home.<br/><b>Planned action:</b> stand near the hallway door while remaining visible.<br/><b>Actual absence:</b> none.<br/><b>Observed:</b> dog lifted head briefly, then returned to resting posture.<br/><b>Recording key:</b> comfortable, based on usual resting behaviour.<br/><b>Next note:</b> review with the existing plan; do not infer readiness for a closed door.'),
('h','A clearly recorded uncertainty'),('p','<b>Context:</b> another day; dog moved out of camera view.<br/><b>Observed:</b> could not see posture or movement.<br/><b>Recording key:</b> uncertain.<br/><b>Action taken:</b> returned and ended the activity.<br/><b>Next note:</b> adjust camera before any further exercise.'),
('h','Why this is useful'),('p','Both records distinguish what happened from what is unknown. Neither uses a vague "passed" label or treats silence as enough evidence. The next step remains a decision, not an automatic longer duration.'),
('p','Use the same standard for your own notes: short, observable and honest. The blank workbook contains more room for writing than this example.')])
add('Terms and further reading','14 / REFERENCES',[
('h','A short glossary'),('p','<b>Comfortable starting point:</b> an action currently observed to be manageable.<br/><b>Desensitisation:</b> carefully graded exposure used in behaviour work.<br/><b>Counterconditioning:</b> changing an association through pairing with something positive.<br/><b>Departure cue:</b> something that may predict leaving.<br/><b>Management:</b> arrangements that help meet the dog\'s needs in daily life.'),
('h','Further reading'),('p','[1] ASPCA. <link href="https://www.aspca.org/pet-care/dog-care/common-dog-behavior-issues/separation-anxiety" color="#A86A3D">Separation Anxiety</link>. Medical assessment and professional support for individual behaviour plans.'),
('p','[2] RSPCA. <link href="https://www.rspca.org.uk/adviceandwelfare/pets/dogs/behaviour/separationrelatedbehaviour" color="#A86A3D">Separation Anxiety in Dogs</link>. Recognising separation-related behaviour, observation and seeking help.'),
('p','[3] Merck Veterinary Manual. <link href="https://www.merckvetmanual.com/behavior/behavior-of-dogs/behavior-problems-of-dogs" color="#A86A3D">Behavior Problems of Dogs</link>. Professional reference on behavioural assessment and management.'),
('h','About this edition'),('p','Revised from the owner-supplied Bea\'s Calm-Alone Protocol. Educational guide and organisational workbook; not a veterinary prescription or a clinically validated programme. Referenced organisations have not endorsed this product. Individual outcomes and timescales vary.'),
('p','Edition 2 / September 2026. Copyright Bea &amp; Co. Personal use: save and print copies for your household. Do not redistribute or resell the files. Keep the workbook private when it contains personal information.')])

def base(c,num,label='THE CALM-ALONE KIT'):
 c.setFillColor(cream);c.rect(0,0,W,H,fill=1,stroke=0)
 c.setFillColor(ink);c.setFont('Helvetica-Bold',11);c.drawString(45,H-38,'BEA & CO.')
 c.setFont('Helvetica',8);c.setFillColor(muted);c.drawRightString(W-45,H-38,label)
 c.setStrokeColor(HexColor('#D9DED1'));c.line(45,43,W-45,43)
 c.setFont('Helvetica',8);c.drawString(45,28,'Small steps. Thoughtful care.');c.drawRightString(W-45,28,str(num))
def title(c,t,k):
 c.setFillColor(gold);c.setFont('Helvetica-Bold',9);c.drawString(45,H-82,k)
 p=Paragraph(t,ParagraphStyle('T',fontName='Times-Roman',fontSize=30,leading=34,textColor=ink))
 _,h=p.wrap(W-90,100);p.drawOn(c,45,H-99-h);return H-116-h

def story(c,blocks,top):
 flows=[]
 for typ,txt in blocks: flows.append(Paragraph(txt,head if typ=='h' else body))
 frame=Frame(45,62,W-90,top-62,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
 frame.addFromList(flows,c)
 if flows: raise RuntimeError('Content overflow: '+str(flows[0].text[:60]))

c=canvas.Canvas(str(OUT/'Beas-Calm-Alone-Guide.pdf'),pagesize=(W,H));c.setTitle("Bea's Calm-Alone Guide");c.setAuthor('Bea & Co.')
base(c,1)
c.setFont('Helvetica-Bold',10);c.setFillColor(gold);c.drawString(45,738,'A PRACTICAL GUIDE + WORKBOOK')
c.setFillColor(ink);c.setFont('Times-Roman',43)
for y,t in [(677,"Bea's"),(629,'Calm-Alone'),(581,'Guide')]:c.drawString(45,y,t)
# Original user photo placed without retouching.
c.drawImage(ImageReader(str(photo)),330,477,width=220,height=293,mask='auto')
story(c,[('p','Understand the moments around leaving.<br/>Keep track of the small steps.<br/>Make room for your dog\'s individual needs.'),('p','An owner-created educational companion.<br/>No fixed timetable. No promised cure.')],443)
c.showPage();base(c,2);y=title(c,'Your guide at a glance','CONTENTS')
for i,p in enumerate(pages):
 py=y-20-i*32
 c.setFillColor(ink);c.setFont('Helvetica',11);c.drawString(45,py,p['title']);c.drawRightString(W-45,py,str(i+3))
 c.linkAbsolute(p['title'],'p'+str(i+3),(45,py-5,W-45,py+15),thickness=0)
c.showPage()
for i,p in enumerate(pages,3):
 c.bookmarkPage('p'+str(i));c.addOutlineEntry(p['title'],'p'+str(i),0,False)
 base(c,i);y=title(c,p['title'],p['kicker']);story(c,p['blocks'],y);c.showPage()
c.save()
(ROOT/'source/guide-content.json').write_text(json.dumps(pages,indent=2))
# Workbook: spacious real AcroForm fields; same fields support printing.
c=canvas.Canvas(str(OUT/'Beas-Calm-Alone-Workbook.pdf'),pagesize=(W,H));c.setTitle("Bea's Calm-Alone Workbook");c.setAuthor('Bea & Co.')
fieldnames=[]
def field(name,label,y,height=36,width=W-90,x=45,multi=False):
 c.setFillColor(ink);c.setFont('Helvetica-Bold',10);c.drawString(x,y,label)
 c.acroForm.textfield(name=name,tooltip=label,x=x,y=y-height-10,width=width,height=height,fontName='Helvetica',fontSize=10,borderWidth=.7,borderColor=HexColor('#9EAA9A'),fillColor=white,textColor=ink,fieldFlags='multiline' if multi else '',maxlen=1600 if multi else 140)
 fieldnames.append(name)

def wbpage(n,t,k,desc):
 base(c,n,'FILLABLE + PRINTABLE WORKBOOK');y=title(c,t,k)
 p=Paragraph(desc,small);_,h=p.wrap(W-90,80);p.drawOn(c,45,y-h);return y-h-30

y=wbpage(1,'Our starting point','01 / SAVE YOUR OWN COPY','Save a copy before typing. Use a PDF reader that supports forms. Save, close and reopen to check your entries. Blank pages can also be printed. This is a record, not a diagnostic test.')
for name,label,height in [('dog','Dog name / date',30),('context','What happens around leaving?',65),('easy','Known comfortable situations (not a maximum-duration test)',65),('signals','What does relaxed behaviour look like for my dog?',65),('questions','Questions for our veterinarian or behaviour professional',65)]:
 field(name,label,y,height,multi=height>30);y-=height+45
c.showPage()
y=wbpage(2,'A plan for daily life','02 / SUPPORT & COVER','Plan the full absence. Confirm your dog is comfortable with the person and setting. Keep contact details private.')
for name,label,height in [('needs','Dates / times when company is needed',55),('support','Who can stay, where, and for which hours?',70),('backup','Backup arrangement if plans change',70),('care','Care instructions / agreed response if the dog struggles',70)]:
 field(name,label,y,height,multi=True);y-=height+48
c.showPage()
y=wbpage(3,'One session, clearly recorded','03 / DUPLICATE THIS PAGE','Use one page per session. Describe what you saw; do not infer calm from silence or eating alone. This recording key is not a clinical scale.')
field('session_date','Date / time',y,28,235);field('session_unit','Actual time + unit (sec / min / none)',y,28,235,315);y-=73
for name,label,height in [('planned','Planned action and context',45),('observed','What actually happened? Body, movement, sound, recovery',65),('key','Comfortable / uncertain / distress - and why?',42),('next','Action taken and next question / easier step',50)]:
 field(name,label,y,height,multi=True);y-=height+44
c.showPage()
y=wbpage(4,'A weekly check-in','04 / PATTERNS, NOT RECORDS','Review comfort and context. The longest absence is not the goal. Leave gaps when no practice happened.')
for name,label,height in [('week','Week beginning',28),('comfortable','Comfortable situations observed this week',62),('changed','Uncertainty, difficulties or changes in routine',62),('worked','Support arrangements that worked',62),('review','Questions / plan to review with our professional',62)]:
 field(name,label,y,height,multi=height>28);y-=height+43
c.showPage()
y=wbpage(5,'When plans change','05 / SETBACK RECORD','Describe the event without blame. If distress or injury occurs, stop practice and seek appropriate help. Do not automatically repeat a previous duration.')
for name,label,height in [('setback_date','Date / situation',28),('event','What happened and what did I observe?',65),('factors','Possible context changes (mark guesses as uncertain)',65),('response','What support or easier arrangement did we use?',65),('followup','Recovery observations / professional follow-up needed',65)]:
 field(name,label,y,height,multi=height>28);y-=height+43
c.showPage();c.save()
# One-page quick reference
c=canvas.Canvas(str(OUT/'Beas-Quick-Reference.pdf'),pagesize=(W,H));c.setTitle('Bea & Co. Quick Reference');c.setAuthor('Bea & Co.');base(c,1,'QUICK REFERENCE')
y=title(c,'Small steps. Clear notes.','KEEP BESIDE YOUR WORKBOOK')
story(c,[('p','Read the guide first. This page is a reminder, not an individual training plan.'),('h','BEFORE'),('p','Dog settled. Comfortable space. Live view working. A manageable action planned. You can return immediately. Support arranged for necessary absences.'),('h','DURING'),('p','Observe the whole dog. Stick to the planned action. If distress appears or the view is lost, return promptly and end the exercise. Do not wait for silence.'),('h','AFTER'),('p','Allow recovery. Record the action, actual duration and unit, body language, sounds and uncertainties. Do not increase difficulty automatically.'),('h','YOUR RECORDING KEY'),('p','Comfortable: matches the dog\'s relaxed baseline.<br/>Uncertain: pause and review.<br/>Distress: stop and seek an easier, supported plan.'),('h','WHEN TO ASK FOR HELP'),('p','Speak to your veterinarian about suspected separation-related distress or changes in health or behaviour. Injury, frantic escape attempts or severe distress need prompt help.'),('p','Educational support from Bea &amp; Co. No fixed recovery time or guaranteed outcome. Keep the full guide and your professional\'s advice alongside this sheet.')],y);c.showPage();c.save()
# Preview is deliberately limited to cover, contents and the fictional example.
r=PdfReader(OUT/'Beas-Calm-Alone-Guide.pdf');w=PdfWriter()
for i in [0,1,14]:w.add_page(r.pages[i])
# Remove internal destinations that point outside sample.
for p in w.pages:
 if '/Annots' in p: del p['/Annots']
with open(ROOT/'output/brand/guide-preview.pdf','wb') as f:w.write(f)
fields=PdfReader(OUT/'Beas-Calm-Alone-Workbook.pdf').get_fields()
assert set(fields)==set(fieldnames)
print('GUIDE',len(r.pages),'pages; WORKBOOK',len(fields),'fillable fields')
