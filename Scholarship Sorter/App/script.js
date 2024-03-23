console.log(MasterList)

// Function to update the MasterList with deadline information
function updateDates(MasterList) {
   const date = new Date();
   const current_date = date.getTime(); // Get current date in milliseconds

   // Loop through each scholarship in the MasterList
   for (let i = 0; i < MasterList.length; i++) {
      const scholarship = MasterList[i];

      // Check if scholarship has a valid deadline
      if (scholarship[2]) {
         const deadline_date = new Date(scholarship[2].replace(/\//g, '-')); // Change slashes to hyphens in the date
         const deadline_timestamp = deadline_date.getTime(); // Get deadline date in milliseconds
         const date_difference = Math.floor((deadline_timestamp - current_date) / (1000*60*60*24)); // Convert milliseconds to days

         // Update deadline information in the scholarship
         if (deadline_timestamp > current_date) {
            scholarship[2] = `${scholarship[2]} <span style="color:#008000;"> Accepting Applications </span> (${date_difference} days until)`;
         } else {
            scholarship[2] = `${scholarship[2]} <span style="color:#ff0000;"> Past Due </span> (${Math.abs(date_difference)} days late)`;
         }
      }
   }
}
updateDates(MasterList);

// Create a table of the MasterList to make it easier on the eyes
function createTable(array, searchString) {
   html = `<thead>
      <tr>
         <th>Scholarship Name</th>
         <th>Opening Date</th>
         <th>Deadline</th>
         <th>Is Essay Required</th>
         <th>Is Need-Based</th>
         <th>Is Merit-Based</th>
         <th>Application (URL)</th>
         <th>Program (URL)</th>
         <th>Degree Seeking</th>
         <th>Enrollment Status</th>
         <th>Citizenship Statuses</th>
         <th>Demographics</th>
         <th>Current Grade Level</th>
         <th>Miscellaneous</th>
         <th>Activity</th>
         <th>Affiliation</th>
         <th><span style="color:#93b2ec;">▀▀▀▀▀▀▀</span>Armed<span style="color:#93b2ec;">▀▀▀▀▀▀▀</span><br><span style="color:#93b2ec;">▀▀▀▀▀▀▀</span>Services<span style="color:#93b2ec;">▀▀▀▀▀▀▀</span></th>
         <th>Situation</th>
         <th>Profession</th>
         <th>Financial Information</th>
         <th>Application Restriction</th>
         <th>Academics</th>
         <th>Condition</th>
         <th>Fields Of Study</th>
         <th><span style="color:#93b2ec;">▀▀▀▀▀</span>Location<span style="color: #93b2ec;">▀▀▀▀▀</span></th>
         <th>Interests</th>
         <th>Study Abroad</th>
         <th>Age</th>
         <th>Scholar ID | CollegeBoard URL | # of Columns</th>
      </tr>
   </thead> <tbody>`;

   for (var i = 0; i < array.length; i++) {
      html += `<tr>`;
      for (var j = 0; j < array[i].length; j++) {
         var cellContent = array[i][j];

         // More formatting!
         if (j === 6) { // applicationUrl
            cellContent = `<button class="button" onclick="openWebsite('${cellContent}')">Apply</button>`;
         } else if (j === 7) { // programUrl)
            cellContent = `<button class="button" onclick="openWebsite('${cellContent}')">View Program</button>`;
         }

         // If the cell content contains the search string, highlight it
         else if (cellContent.toLowerCase().includes(searchString.toLowerCase())) {
            var regex = new RegExp(`(${searchString})`, 'gi');
            cellContent = cellContent.replace(regex, '<span class="searched_text">$1</span>');
         }
         html += `<td>${cellContent}</td>`;
      }
      html += '</tr>';
   }
   html += '</tbody>'
   return html;
}

function openWebsite(url) { // Open the website in a new tab when the button is clicked
   window.open(url, '_blank');
}

function toggleRow(row) { // Expands the row of the table once clicked on
   row.classList.toggle('expanded');
}

// Searches for a certain string in the MasterList and displays a table of each thingy
function search(MasterList) {
   var searchString = (document.getElementById('textbox_search').value).toLowerCase();
   var instances = new Set(); // Use a Set to store unique instances

   var acceptingApplicationsOnly = document.getElementById('accepting_applications_checkbox').checked;
   var isEssayRequired = document.getElementById('is_essay_required_checkbox').checked;
   var isNeedBased = document.getElementById('is_need_based_checkbox').checked;
   var isMeritBased = document.getElementById('is_merit_based_checkbox').checked;
   
   var filters = {
      "acceptingApplicationsOnly": acceptingApplicationsOnly,
      "isEssayRequired": isEssayRequired,
      "isNeedBased": isNeedBased,
      "isMeritBased": isMeritBased
   }
   //console.log(filters)

   function searchList(list, searchString, filters) {
      list.forEach(item => {
         // Apply filters based on checkbox states
         if (filters.acceptingApplicationsOnly && list[2].includes('Past Due')) {
            return; // Skip if not accepting applications
         }
         if (filters.isEssayRequired && item[3] === "Yes") {
            return; // Skip if essay is not required
         }
         if (filters.isNeedBased && item[4] === "Yes") {
            return; // Skip if not need-based
         }
         if (filters.isMeritBased && item[5] === "Yes") {
            return; // Skip if not merit-based
         }
   
         // Check if the item matches the search string
         if (searchString && typeof item === 'string' && item.toLowerCase().includes(searchString)) {
            instances.add(list); // Add the entire list to the Set
            return; // Exit the loop if an instance is found
         } else if (Array.isArray(item)) {
            searchList(item, searchString, filters); // Recursively search nested lists
         }
      });
   }

   searchList(MasterList, searchString, filters); // Start the search
   var uniqueInstances = Array.from(instances); // Convert Set back to an array
   var table = createTable(uniqueInstances, searchString);
   document.getElementById('myTable').innerHTML = table;
   
   // Update the label showing the length of the list
   document.getElementById('listLengthLabel').textContent = `Total items: ${uniqueInstances.length}`;
}
