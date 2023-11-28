Curriculuum <br>
**Short Specializations** <br>

# Queuing System in JavaScript (0x03)

## Overview
This comprehensive project focuses on building a robust queuing system in JavaScript, leveraging the power of Redis, Node.js, and the Kue library. The queuing system is designed to handle asynchronous tasks efficiently, making it suitable for scenarios ranging from background job processing to managing complex workflows. The project is structured into distinct tasks, each addressing specific components and functionalities.

## Project Purpose
The primary purpose of this project is to demonstrate the implementation of a queuing system that utilizes Redis as a backend data store and Node.js for server-side logic. The Kue library is employed to streamline the management of background jobs, making it easier to create, process, and monitor tasks asynchronously.

## Key Features
- **Redis Integration:** The project emphasizes a seamless integration with Redis, a powerful in-memory data structure store, to efficiently manage task-related data.

- **Node.js Backend:** Leveraging the event-driven, non-blocking I/O model of Node.js, the system provides a scalable and performant backend for handling asynchronous tasks.

- **Kue Library:** The Kue library facilitates the creation and processing of jobs, enabling developers to focus on task-specific logic rather than intricate queuing mechanisms.

- **Web Application Components:** The project extends beyond basic queuing functionality to include practical implementations such as a stock management system and a seat reservation system, showcasing the versatility of the queuing system in real-world scenarios.

## Project Structure
The project is organized into multiple tasks, each progressively building upon the previous one. This structured approach allows developers to explore and understand the components of the queuing system in a step-by-step manner.

1. **Task 0: Redis Setup**
   - File: `dump.rdb`
   - Instructions to install and configure Redis.

2. **Task 1: Node Redis Client**
   - File: `0-redis_client.js`
   - A script that connects to a Redis server and logs connection status.

3. **Task 2: Node Redis Client and Basic Operations**
   - File: `1-redis_op.js`
   - Extends the previous script to perform basic Redis operations like setting and getting values.

4. **Task 3: Node Redis Client and Async Operations**
   - File: `2-redis_op_async.js`
   - Modifies the previous script to use async/await for Redis operations.

5. **Task 4: Node Redis Client and Advanced Operations**
   - File: `4-redis_advanced_op.js`
   - Utilizes Redis to store and retrieve hash values.

6. **Task 5: Node Redis Client Publisher and Subscriber**
   - Files: `5-subscriber.js`, `5-publisher.js`
   - Implements a publisher-subscriber system using Redis.

7. **Task 6: Job Creator and Processor**
   - Files: `6-job_creator.js`, `6-job_processor.js`
   - Creates and processes jobs using the Kue library.

8. **Task 7: Track Progress and Errors with Kue**
   - Files: `7-job_creator.js`, `7-job_processor.js`
   - Enhances the job processing to track progress and handle errors.

9. **Task 8: Writing Job Creation Function**
   - Files: `8-job.js`, `8-job-main.js`, `8-job.test.js`
   - Implements a function to create and test job creation.

10. **Task 9: Stock Management System**
    - File: `9-stock.js`
    - Implements a web application to manage product stock using Redis and Express.

11. **Task 100: Seat Reservation System**
    - File: `100-seat.js`
    - Implements a seat reservation system using Redis, Kue, and Express.

## How to Run
1. Ensure you have Node.js and npm installed.
2. Clone the repository: `git clone https://github.com/your-username/queuing-system-in-js.git`
3. Navigate to the project directory: `cd queuing-system-in-js`
4. Install dependencies: `npm install`
5. Follow the instructions in each task to run the specific scripts.

## Dependencies
- Redis
- Node.js
- Express
- Kue
- Other specified dependencies in the `package.json` file.

## Notes
- Make sure to run `npm install` to install the required dependencies before executing any scripts.
- Ensure a Redis server is running and accessible.

## Contributors
- [Your Name]
- [Contributor 1]
- [Contributor 2]
