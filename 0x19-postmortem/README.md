<h1>Incident Report</h1>
<h2>Incident Summary</h2>
<p>On September 10, 2023, at 12:45 AM GMT +3, the user authentication service experienced a complete outage of services. The outage lasted for 45 minutes and resulted in a 30% decrease in overall system usage. </p>
<h2>Root Cause</h2>
<p>The main culprit was a misconfiguration in the load balancer settings. A recent update to the load balancer configuration inadvertently led to excessive load distribution among backend servers. This imbalance caused server nodes to exceed their capacity, resulting in degraded service performance and eventual unavailability. Luckily we caught this early enough</p>
<h2>Timeline</h2>
<li>
<ul>12:45 AM: Monitoring systems triggered alerts for increased error rates and latency in the user authentication service.</ul>
<ul>12:50 AM: The incident response team initiated an investigation to identify the cause of the sudden service degradation.</ul>
<ul>01:00 AM: Initial assumptions were centered around potential database issues due to historical similar incidents.</ul>
<ul>01:15 AM: Recognizing the persistence of the issue, the incident was escalated to the engineering leadership team for further review and decision-making.</ul>
<ul>01:25 AM: After a brief discussion among the engineering leadership, the root cause of the misconfigured load balancer was identified, and corrective actions were planned.</ul>
<ul>01:30 AM: The incident was resolved by reverting the load balancer configuration to its previous state and thoroughly testing the service to ensure a return to normal operation.</ul>
</li>
<h2>Corrective and Preventative Measures</h2>
<p>The following corrective and preventative measures have been taken to address the issue and prevent future occurrences:</p>
<li>
<ul>A thorough review of configuration changes will be conducted before deployment to identify potential misconfigurations.</ul>
<ul>Automated tests will be implemented for load balancer configuration to catch distribution imbalances during the development and testing phases.</ul>
<ul>Real-time monitoring and alerting will be enhanced to quickly detect and respond to sudden spikes in error rates and service degradation.</ul>
<ul>Clear communication channels will be established for incident escalation to ensure timely involvement of relevant stakeholders.</ul>
<ul>Regular training sessions will be conducted for the operations team to improve incident response capabilities and reduce the chances of misleading investigations.</ul>
</li>
<h2>Tasks to Address the Issue</h2>
<p>The following tasks will be completed to address the issue:</p>
<li>
<ul>The release process will be reviewed to implement stricter checks on configuration changes before deployment.</ul>
<ul>Automated tests will be developed and integrated for load balancer configuration adjustments.</ul>
<ul>Monitoring tools will be updated to provide real-time insights into traffic distribution and backend server performance.</ul>
<ul>An incident response playbook will be created with predefined escalation paths and clear responsibilities.</ul>
<ul>Incident response training will be conducted to ensure prompt response and recovery during service outages.</ul>
</li>


