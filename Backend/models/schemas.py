from ast import keyword
from typing import Any, Dict, List, Optional
from pydantic import BaseModel
class component(BaseModel):
    formatting:float
    keywords:float
    content:float
    skill_validation:float
    ats_compatibility:float
class JDComponentScore(BaseModel):
     match_perentage:float
     ats_compatibility:float
class JDComparison(BaseModel):
    match_percentage:float
    semantic_similarity:float
    matched_keywords:List[str]
    matched_keywords:List[str]
    skills_gap:List[str]

class SkillValidation(BaseModel):
    validated:List[Dict[str,Any]]
    unvalidated:List[str] =[]
    validation_count :int =0
    validation_percentage:float =0.0

class IssueDetail(BaseModel):
    issue_title:str
    severity_level:str
    ats-impact:str
    explaination:str
    where_it_appears:str
    how_to_fix:str
    action_items:List[str]
    example_improvement:str

class AnalysisResposnse(BaseModel):
    ATS_score:float
    component_scores: component_scores
    issues_summary:List[str]
    detailed_feedback:List[str]
    jd_match_analysis:List[IssueDetail]
    skill_validation_details:Optional[SkillValidation]=None
    ats_score:float
    keyword match:float=0.0

    
    
    