
// script.js

document.addEventListener('DOMContentLoaded', function () {
    const students = ['John Doe', 'Jane Smith', 'Sam Wilson', 'Emily Johnson'];

    // Populate year dropdown (e.g., 2020 - 2030)
    const yearSelect = document.getElementById('year');
    const currentYear = new Date().getFullYear();
    for (let i = 2024; i <= currentYear + 1; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = i;
        if (i === currentYear) {
            option.selected = true;
        }
        yearSelect.appendChild(option);
    }

    // Define months
    const months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'];

    // Get the current month
    const currentMonth = new Date().getMonth(); // January is 0

    // Create month tabs and corresponding tab panes
    months.forEach((month, index) => {
        createMonthTab(month, index);
        createMonthTable(month, index, students);
    });

    // Automatically set the current month as active
    document.getElementById(`v-pills-${months[currentMonth]}-tab`).classList.add('active');
    document.getElementById(`${months[currentMonth]}`).classList.add('show', 'active');

    // Function to create the month tab
    function createMonthTab(month, index) {
        const nav = document.getElementById('v-pills-tab');
        const button = document.createElement('button');
        button.className = 'nav-link';
        button.id = `v-pills-${month}-tab`;
        button.setAttribute('data-bs-toggle', 'pill');
        button.setAttribute('data-bs-target', `#${month}`);
        button.type = 'button';
        button.role = 'tab';
        button.textContent = capitalizeFirstLetter(month);
        nav.appendChild(button);
    }

    // Function to create the month table (content)
    function createMonthTable(month, index, students) {
        const tabContent = document.getElementById('v-pills-tabContent');
        const div = document.createElement('div');
        div.className = 'tab-pane fade';
        div.id = month;
        div.role = 'tabpanel';
        
        const table = document.createElement('table');
        table.className = 'table table-bordered';

        // Create table head
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        headerRow.innerHTML = '<th>Student Name</th>';

        // Get Mondays, Wednesdays, Fridays for this month
        const days = getMondaysWednesdaysFridays(currentYear, index + 1);

        days.forEach(day => {
            const th = document.createElement('th');
            th.textContent = day.toDateString();
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);

        // Create table body
        const tbody = document.createElement('tbody');
        students.forEach(student => {
            const row = document.createElement('tr');
            let studentColumn = `<td>${student}</td>`;

            days.forEach(day => {
                studentColumn += `
                    <td>
                        <div class="attendance-btn">
                            <span class="icon">&#x2713;</span>
                            <span>Present</span>
                            <div class="options">
                                <button onclick="markAttendance('${student}', '${month}', '${day.toDateString()}', '')">
                                    <span class="icon">&#x2713;</span>
                                </button>
                                <button onclick="markAttendance('${student}', '${month}', '${day.toDateString()}', '')">
                                    <span class="icon">&#x2717;</span>
                                </button>
                            </div>
                        </div>
                    </td>
                `;
            });

            row.innerHTML = studentColumn;
            tbody.appendChild(row);
        });

        table.appendChild(thead);
        table.appendChild(tbody);
        div.appendChild(table);
        tabContent.appendChild(div);
    }

    // Function to get Mondays, Wednesdays, and Fridays of a month
    function getMondaysWednesdaysFridays(year, month) {
        const days = [];
        const date = new Date(year, month - 1, 1);

        while (date.getMonth() === month - 1) {
            if (date.getDay() === 1 || date.getDay() === 3 || date.getDay() === 5) { // Monday = 1, Wednesday = 3, Friday = 5
                days.push(new Date(date));
            }
            date.setDate(date.getDate() + 1);
        }

        return days;
    }

    // AJAX function to mark attendance
    window.markAttendance = function (student, month, day, status) {
        const year = document.getElementById('year').value;
        const attendanceData = {
            student,
            year,
            month,
            day,
            status
        };

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/markAttendance', true);
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                alert(`${student}'s attendance for ${day} marked as ${status}`);
            }
        };
        xhr.send(JSON.stringify(attendanceData));
    }

    // Helper function to capitalize the first letter of a string
    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
});

