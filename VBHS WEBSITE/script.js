function toggleCollapse(id, header_id) {
    const element = document.getElementById(id);
    const header = document.getElementById(header_id);
    
    if (element.style.display === 'none') {
        element.style.display = 'block';
        header.style.setProperty('--icon', '"⮟"'); // Change icon to right
        } else {
        element.style.display = 'none';
        header.style.setProperty('--icon', '"➤"'); // Change icon to down
    }
}

function newElement(typeOfElement, parent, text, id, class_) {
    const newElement = document.createElement(typeOfElement);
    if (text   != '') { newElement.textContent = text; }
    if (id     != '') { newElement.id = id; }
    if (class_ != '') { newElement.className = class_; }
    document.getElementById(parent).appendChild(newElement);
}

function addClassToBefore(headerSelector, className) {
    const header = document.querySelector(headerSelector);
    if (header) {
        header.classList.add(className);
    }
}

const tableCells = document.querySelectorAll('td');
let courseContainer;

// Main Iteration Logic
for (const [subject, offerings] of Object.entries(courses)) {
    newElement('div', 'classContainer', '', subject, 'subjectContainer'); // Container for each subject (holds offerings)
    newElement('h1', subject, subject, '', 'subjectHeader'); // Heading for the subject
    
    for (const [offering, coursesArray] of Object.entries(offerings)) {
        newElement('div', subject, '', offering, 'offeringContainer'); // Container for offeringHeader and offeringContainer_contents
        newElement('h2', offering, offering, `${offering}_header`, 'offeringHeader'); // Header for the offering type
        newElement('div', offering, '', `${offering}_contents`, 'offeringContainer_contents'); // Container for each offering (holds specific courses)

        // Initialize the offering container as closed
        const offeringContents = document.getElementById(`${offering}_contents`);
        offeringContents.style.display = 'none'; // Hide the contents by default
        
        // Set the header icon to the closed state
        const offeringHeader = document.getElementById(`${offering}_header`);
        offeringHeader.style.setProperty('--icon', '"➤"'); // Icon pointing to the right
        offeringHeader.addEventListener('click', function() {
            toggleCollapse(`${offering}_contents`, `${offering}_header`);
        });

        for (const course of coursesArray) {
            // Create course elements as before
            newElement('div', `${offering}_contents`, '', `${course.name}_courseContainer`, 'courseContainer');

            // Use fancy logic to get a cool string like ○○●●○
            let gradesIndicator = "";
            for (let i = 0; i < course.grades.length; i+=2) {
                if      (course.grades[i] && course.grades[i+1])   {gradesIndicator += "●"} // true true
                else if (course.grades[i] && !course.grades[i+1])  {gradesIndicator += "◐"} // true false
                else if (!course.grades[i] && course.grades[i+1])  {gradesIndicator += "◑"} // false true
                else if (!course.grades[i] && !course.grades[i+1]) {gradesIndicator += "○"} // false false
            }

            newElement('h3', `${course.name}_courseContainer`, `${course.name}\u00A0 ${gradesIndicator}`, `${course.name}_courseHeader`, 'courseHeader');
            
            const ulDetails = document.createElement('ul');
            document.getElementById(`${course.name}_courseContainer`).appendChild(ulDetails);
            
            // Apply details ///////////////////////////////////////////////////////////////////////////////////
            const courseHeader = document.getElementById(`${course.name}_courseHeader`);
            let details = [];

            details.push(`${course.description}`);

            if (course.prerequisite && course.prerequisite.length > 0) { details.push(`Prerequisite(s): ${course.prerequisite.join(', ')}`); }
            details.push(`Credits: ${course.credits}`);

            if (course.honors) {
                details.push(`*Honors Course*`);
                courseHeader.classList.add('honors');
            }

            if (course.advancedPlacement) {
                details.push(`**AP Course**`);
                courseHeader.classList.add('advancedPlacement');
            }

            if (course.CONC) {
                details.push(`**CONC Course through ${course.CONC}**`);
                courseHeader.classList.add('CONC');
            }
            ////////////////////////////////////////////////////////////////////////////////////////////////////

            let courseCodeString = (course.courseCode != -1 ? `#${course.courseCode}` : 'WATC');
            newElement('p', `${course.name}_courseContainer`, courseCodeString, '', 'courseCode');

            for (const detail of details) {
                const detailLi = document.createElement('li');
                detailLi.textContent = detail;
                ulDetails.appendChild(detailLi);
            }
        }
    }
}

function findAllowedGrades(grades) {
    let allowedGrades = [];
    for (let i = 0; i < grades.length; i++) {
        if (grades[i]) {
            allowedGrades.push(i+1);
        }
    }
    return allowedGrades;
}

function getLeftmostTH(elementUnderCursor) {
    // Ensure the elementUnderCursor is a table cell (TD or TH)
    if (elementUnderCursor && (elementUnderCursor.tagName === 'TD' || elementUnderCursor.tagName === 'TH')) {
        const row = elementUnderCursor.parentElement;
        const leftmostCell = row.querySelector('td, th'); // Selects the first TD or TH in the row
        return leftmostCell ? leftmostCell.textContent : null;
    }
    return null;
}

function checkForQualities(course, elementUnderCursor, courseContainer) {
    elementUnderCursor.textContent = course.name;
    elementUnderCursor.classList.add('occupied');
    if (course.honors) { elementUnderCursor.classList.add('honors'); }
    if (course.advancedPlacement) { elementUnderCursor.classList.add('advancedPlacement'); }
    if (course.CONC) { elementUnderCursor.classList.add('CONC'); }
    courseContainer.classList.add('used');
}


for (const [subject, offerings] of Object.entries(courses)) {
    for (const [offering, coursesArray] of Object.entries(offerings)) {
        for (const course of coursesArray) {

            const courseElement = document.getElementById(`${course.name}_courseContainer`);
            courseElement.addEventListener('click', function (event) {
                if (courseElement.classList.contains('used')) return;

                const courseContainer = document.querySelector(`[id="${course.name}_courseContainer"]`);
                courseContainer.classList.add('clicked'); // Start the rotation

                // Create the mousebox
                const mouseBox = document.createElement('div');
                mouseBox.classList.add('mouseBox');
                if (course.honors) { mouseBox.classList.add('honors'); }
                if (course.CONC) { mouseBox.classList.add('CONC'); }
                if (course.advancedPlacement) { mouseBox.classList.add('advancedPlacement'); }
                mouseBox.textContent = course.name;
                document.body.appendChild(mouseBox);

                function moveBox(e) {
                    mouseBox.style.position = 'absolute';
                    mouseBox.style.left = `${e.pageX - 40}px`; // Offset by 40px
                    mouseBox.style.top = `${e.pageY - 40}px`; // Offset by 30px

                    tableCells.forEach(cell => {
                        const isAllowedSubject = [subject, "Elective 1", "Elective 2", "Elective 3"].includes(getLeftmostTH(cell));
                        const isAllowedGrade = findAllowedGrades(course.grades).includes(Number(cell.id[1]));
                        if (!(isAllowedSubject && isAllowedGrade)) {
                            cell.classList.add('unavailable');
                        }
                    });
                }

                function resetAvailability() {
                    tableCells.forEach(cell => cell.classList.remove('unavailable'));
                }

                function handleDrop(e) {
                    let elementUnderCursor = document.elementFromPoint(e.clientX, e.clientY);

                    if (
                        elementUnderCursor &&
                        elementUnderCursor.tagName === 'TD' &&
                        [subject, "Elective 1", "Elective 2", "Elective 3"].includes(getLeftmostTH(elementUnderCursor)) &&
                        findAllowedGrades(course.grades).includes(Number(elementUnderCursor.id[1]))
                    ) {
                        if (course.credits === 1 || course.credits === 2) {
                            if (Number(elementUnderCursor.id[1]) % 2 === 0) {
                                elementUnderCursor = elementUnderCursor.previousElementSibling;
                            }
                            const nextCell = elementUnderCursor.nextElementSibling;

                            if (nextCell && nextCell.tagName === 'TD' && !nextCell.textContent.trim()) {
                                elementUnderCursor.setAttribute('colspan', '2');
                                nextCell.style.display = 'none';
                                checkForQualities(course, elementUnderCursor, courseContainer);
                            } else {
                                console.log('Cannot place 1 or 2-credit course in this location');
                            }
                        } else if (!elementUnderCursor.textContent.trim()) {
                            checkForQualities(course, elementUnderCursor, courseContainer);
                        }
                    } else {
                        console.log("Invalid placement. Clearing unavailable cells.");
                    }
                    cleanup();
                }

                // General cleanup function
                function cleanup() {
                    resetAvailability();
                    courseContainer.classList.remove('clicked');
                    document.removeEventListener('mousemove', moveBox);
                    document.removeEventListener('mouseup', handleDrop);
                    mouseBox.remove();
                }
                setTimeout(() => {
                    isMouseStationary = true;
                    console.log('Mouse is stationary');
                    // Your stationary logic here
                }, 300); // Adjust the delay as needed

                document.addEventListener('mousemove', moveBox);
                document.addEventListener('click', function handleClick(event) {
                    moveBox(event); // Trigger moveBox animation on click
                    resetAvailability(); // Clear unavailable cells
                    document.removeEventListener('click', handleClick); // Ensure resetAvailability only runs once
                });
                document.addEventListener('mouseup', handleDrop);
            });
        }
    }
}

// Double-click listener to handle unmerging of cells
tableCells.forEach(cell => {
    cell.addEventListener('dblclick', function() {

        cell.classList.remove('occupied');
        cell.classList.remove('honors');
        cell.classList.remove('advancedPlacement');
        cell.classList.remove('CONC');
        courseContainer = document.querySelector(`[id="${cell.textContent}_courseContainer"]`);
        if (courseContainer) { courseContainer.classList.remove('used'); }

        // If the cell has merged (colspan="2"), unmerge it
        if (cell.getAttribute('colspan') === '2') {
            cell.removeAttribute('colspan');

            // Reset the colspan to 1 and show the next cell
            const nextCell = cell.nextElementSibling;
            cell.style.display = '';
            cell.textContent = '';
            nextCell.textContent = '';
            nextCell.style.display = '';
        } else {
            // Clear the content of the cell and mark it as unoccupied
            cell.textContent = ''; 
        }
    });
});