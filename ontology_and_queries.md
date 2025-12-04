# Nodes





* Machine



 	Properties: productId, type



 	Meaning: a physical machine (L/M/H type) used in production.





* Measurement



 	Properties: udi, airTemperature, processTemperature, rotationalSpeed, torque, toolWear



 	Meaning: one production run (or time point) with its sensor readings.





* Failure



 	Properties: just a structural node linking measurement to failure type.



 	Meaning: the fact that this measurement/run has failure info.





* FailureType



 	Properties: TWF, HDF, PWF, OSF, RNF (booleans)



 	Meaning: which failure modes occurred for this run.







* Relationships



 	(:Machine)-\[:HAS\_MEASUREMENT]->(:Measurement)



 		Meaning: this measurement was produced by that machine.



 	(:Measurement)-\[:HAS\_FAILURE]->(:Failure)



 		Meaning: this measurement has associated failure info.



 	(:Failure)-\[:OF\_TYPE]->(:FailureType)



 		Meaning: which failure modes apply to that run.







Each path Machine → Measurement → Failure → FailureType represents one production run with its machine, sensor readings, and failure modes.











\## Example queries



\### 1. How many runs had each failure type?





MATCH (me:Measurement)-\[:HAS\_FAILURE]->(f:Failure)-\[:OF\_TYPE]->(ft:FailureType)

RETURN

sum(CASE WHEN ft.TWF THEN 1 ELSE 0 END) AS twf\_runs,

sum(CASE WHEN ft.HDF THEN 1 ELSE 0 END) AS hdf\_runs,

sum(CASE WHEN ft.PWF THEN 1 ELSE 0 END) AS pwf\_runs,

sum(CASE WHEN ft.OSF THEN 1 ELSE 0 END) AS osf\_runs,

sum(CASE WHEN ft.RNF THEN 1 ELSE 0 END) AS rnf\_runs;









Explanation: counts how many production runs had each failure type.



\### 2. What are typical conditions when TWF happens?





MATCH (me:Measurement)-\[:HAS\_FAILURE]->(f:Failure)-\[:OF\_TYPE]->(ft:FailureType)

WHERE ft.TWF = true

RETURN avg(me.torque) AS avgTorque, avg(me.toolWear) AS avgToolWear;



Explanation: shows average torque and tool wear during TWF failures.

