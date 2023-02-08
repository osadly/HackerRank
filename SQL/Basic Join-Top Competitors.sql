select hck.hacker_id,hck.name --,count(sbm.submission_id) count_challenges
from Hackers HCK, Difficulty DFC, Challenges CHL, Submissions SBM
Where HCK.Hacker_ID=SBM.hacker_id                                                        
and DFC.difficulty_level=chl.difficulty_level
and chl.challenge_id=sbm.challenge_id
and sbm.score=dfc.score
group by hck.hacker_id,hck.name
having count(sbm.submission_id)>1
order by count(sbm.submission_id) desc, hacker_id;