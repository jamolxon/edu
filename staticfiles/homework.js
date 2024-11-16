const months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'];

document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const groupId = urlParams.get('group_id');

    if (!groupId) {
        alert('Group ID is required in the URL to load the attendance page.');
        return;
    }

    const currentYear = new Date().getFullYear();

    // Fetch CSRF token from meta tag
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    fetch(`/api/v1/group/${groupId}/`)
        .then(response => response.json())
        .then(groupData => {
            const { name, day_type } = groupData;
            document.getElementById('group-name').textContent = `Homework for ${name}`;

            const yearSelect = document.getElementById('year');
            for (let i = 2024; i <= currentYear + 1; i++) {
                const option = document.createElement('option');
                option.value = i;
                option.textContent = i;
                if (i === currentYear) {
                    option.selected = true;
                }
                yearSelect.appendChild(option);
            }

            const currentMonth = new Date().getMonth();

            fetch(`/api/v1/group/${groupId}/students/`)
                .then(response => response.json())
                .then(studentsData => {
                    const students = studentsData.map(student => ({
                        student_id: student.id,
                        fullName: `${student.first_name} ${student.last_name}`
                    }));

                    months.forEach((month, index) => {
                        createMonthTab(month, index);
                        createMonthTable(month, index, students, day_type);
                    });

                    document.getElementById(`v-pills-${months[currentMonth]}-tab`).classList.add('active');
                    document.getElementById(`${months[currentMonth]}`).classList.add('show', 'active');

                    // Fetch and display attendance data after setting up the tables
                    fetchAttendanceData();
                })
                .catch(error => {
                    console.error('Error fetching student list:', error);
                });
        })
        .catch(error => {
            console.error('Error fetching group information:', error);
        });

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

    function createMonthTable(month, index, students, dayType) {
        const tabContent = document.getElementById('v-pills-tabContent');
        const div = document.createElement('div');
        div.className = 'tab-pane fade';
        div.id = month;
        div.role = 'tabpanel';

        const table = document.createElement('table');
        table.className = 'table table-bordered';

        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        headerRow.innerHTML = '<th>Student Name</th>';

        const days = (dayType === 'mwf')
            ? getMondaysWednesdaysFridays(currentYear, index + 1)
            : getTuesdaysThursdaysSaturdays(currentYear, index + 1);

        days.forEach(day => {
            const th = document.createElement('th');
            th.textContent = day.toDateString();
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);

        const tbody = document.createElement('tbody');
        students.forEach(student => {
            const row = document.createElement('tr');
            let studentColumn = `<td>${student.fullName}</td>`;

            days.forEach(day => {
                const dayString = day.toDateString();
                studentColumn += `
                    <td id="${student.student_id}-${month}-${dayString}">
                        <div class="attendance-btn" style="max-width: 80px; height: 40px;">
                            <span></span>
                            <div class="options">
                                <button onclick="markAttendance('${student.student_id}', '${student.fullName}', '${month}', '${dayString}', 'done')">
                                    <span class="icon">&#x2713;</span>
                                </button>
                                <button onclick="markAttendance('${student.student_id}', '${student.fullName}', '${month}', '${dayString}', 'not_done')">
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

    function getMondaysWednesdaysFridays(year, month) {
        const days = [];
        const date = new Date(year, month - 1, 1);

        while (date.getMonth() === month - 1) {
            if (date.getDay() === 1 || date.getDay() === 3 || date.getDay() === 5) {
                days.push(new Date(date));
            }
            date.setDate(date.getDate() + 1);
        }

        return days;
    }

    function getTuesdaysThursdaysSaturdays(year, month) {
        const days = [];
        const date = new Date(year, month - 1, 1);

        while (date.getMonth() === month - 1) {
            if (date.getDay() === 2 || date.getDay() === 4 || date.getDay() === 6) {
                days.push(new Date(date));
            }
            date.setDate(date.getDate() + 1);
        }

        return days;
    }

    function fetchAttendanceData() {
        fetch(`/api/v1/group/${groupId}/homework/`)
            .then(response => response.json())
            .then(attendanceData => {
                attendanceData.forEach(record => {
                    const { student, homework_date, type } = record;
                    const dayString = new Date(homework_date).toDateString();
                    const monthIndex = new Date(homework_date).getMonth();
                    const monthName = months[monthIndex];
                    
                    const cellId = `${student}-${monthName}-${dayString}`;
                    const cell = document.getElementById(cellId);

                    if (cell) {
                        if (type === 'done'){
                        //cell.innerHTML = `<span class="icon">&#x2713;</span>`;
                        cell.innerHTML = `<div class="attendance-btn" style="background: lightgreen;">
                            <span class="icon">&#x2713;</span>
                        </div>`
                        }
                        else {
                        // cell.innerHTML = `<span class="icon">&#x2717;</span>`;
                        cell.innerHTML = `<div class="attendance-btn" style="background: #FF474D;"> <span class="icon">&#x2717;</span> </div>`
                        }
                    }
                });
            })
            .catch(error => {
                console.error('Error fetching homework data:', error);
            });
    }

    window.markAttendance = function (student_id, studentName, month, day, status) {
        const year = document.getElementById('year').value;
        const date = new Date(day);
        const m = String(date.getMonth() + 1).padStart(2, '0');
        const d = String(date.getDate()).padStart(2, '0');
        const formattedDate = `${year}-${m}-${d}`;

        const attendanceData = {
            group: groupId,
            student: student_id,
            student_name: studentName,
            year,
            month,
            homework_date: formattedDate,
            type: status
        };

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/api/v1/group/homework/create/', true);
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
        xhr.setRequestHeader('X-CSRFToken', csrfToken);  // Include CSRF token in header
        xhr.onreadystatechange = function () {
                fetchAttendanceData(); // Fetch updated attendance data
            }
        xhr.send(JSON.stringify(attendanceData));
    };

    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
});
