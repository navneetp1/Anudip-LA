use WorldEvents;

-- ye poora dekh kr kra hai, just visualize the tables in le head 

select
	Family.FamilyName,
	(CASE
		WHEN TopFamily.FamilyName is null THEN ''
		ELSE TopFamily.FamilyName + ' > '
	END) + 
	(CASE 
		WHEN ParentFamily.FamilyName is null THEN ''
		ELSE ParentFamily.FamilyName + ' > '
	END) + Family.FamilyName as [Family path]
from
	tblFamily as Family 
	-- parent level family 
	left outer join tblFamily as ParentFamily on ParentFamily.FamilyID = Family.ParentFamilyId
	-- grandparent level family
	left join tblFamily as TopFamily on TopFamily.FamilyID = ParentFamily.ParentFamilyId