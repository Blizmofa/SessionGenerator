## What is a Network Session?
A network session refers to a connection or exchange of data between two endpoints in a network. It typically involves the continuous interaction between a client and a server or between two peers. Sessions allow applications to manage ongoing data exchanges by maintaining context, state, and synchronization.

## Key Characteristics of Network Sessions
1. <b>Uniqueness:</b> A session is defined by a unique combination of communication parameters, such as IP addresses, port numbers, and protocol.
2. <b>Stateful Interaction:</b> Sessions often track the state of communication to ensure proper sequencing and data integrity.
3. <b>Lifecycle:</b> Sessions have a start, active state, and termination phase. For instance, in TCP, these are marked by the SYN, data transfer, and FIN flags, respectively.

## How Network Sessions Appear in Wireshark
1. <b>Filter by Protocol:</b> Use display filters such as tcp, udp, or http to narrow down packets for specific protocols.
2. <b>Conversation View:</b> Wireshark groups packets into conversations. Go to Statistics > Conversations to see active sessions, which can include IP, TCP, and UDP sessions.
3. <b>Follow Stream:</b> Right-click on a packet and select Follow TCP/UDP Stream. This shows all packets within a session in sequence, including their payload.
4. <b>Five-Tuple Representation:</b> sessions are often identified by their 5-tuple:
   - Source IP
   - Destination IP
   - Source Port
   - Destination Port
   - Protocol

## Common Sessions
| **Feature**            | **HTTP**                                       | **DNS**                                       | **FTP**                                        | **SMTP**                                       | **SSH**                                         | **Telnet**                                      | **SNMP**                                        |
|------------------------|------------------------------------------------|-----------------------------------------------|------------------------------------------------|-----------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|
| **Protocol**           | TCP (Reliable stream)                         | UDP (Fast query-response), TCP (for large data) | TCP (Two channels: Control and Data)           | TCP (Reliable mail transfer)                  | TCP (Secure shell session)                     | TCP (Insecure terminal session)                | UDP (For device management)                     |
| **Ports**              | 80 (HTTP), 443 (HTTPS)                        | 53 (UDP/TCP)                                  | 21 (Control), 20 (Data in Active mode)         | 25 (SMTP), 587 (SMTPS)                        | 22 (SSH)                                       | 23 (Telnet)                                    | 161 (SNMP), 162 (SNMP Trap)                     |
| **Session Type**       | Stateless (HTTP/1.1 Keep-Alive, HTTP/2/3)     | Stateless query-response cycle                | Stateful, uses both control and data channels  | Stateless (Request/Response)                  | Stateful (Interactive shell)                   | Stateful (Interactive terminal)                | Stateless (Request/Response)                    |
| **Flags**              | SYN, ACK, PSH, FIN                            | QR, RD, AA, TC, etc.                          | SYN, ACK, FIN, Mode (Active/Passive)           | SYN, ACK, FIN, DATA (for email transmission)  | SYN, ACK, FIN, ENCRYPT (for secure shell)      | SYN, ACK, FIN                                  | GET, SET, TRAP, RESPONSE                        |
| **Payload**            | HTML, JSON, images, files, etc.               | Domain name, IP address                       | FTP commands, files, directory listings        | Email headers, body, attachments               | Command execution, session data                | Text commands and responses                    | SNMP MIB (Management Information Base) data    |
| **Session Setup**      | TCP handshake (SYN, SYN-ACK, ACK)             | Simple UDP query                              | Control connection on port 21, Data on port 20 | Simple request-response (Mail command)        | TCP connection setup and authentication       | Connection and authentication with username/password | SNMP request to device or agent                |
| **Session Termination**| FIN flag (TCP connection close)               | No formal termination (stateless)             | QUIT command, both connections closed          | QUIT, FIN commands to terminate session       | SSH session closed after command execution    | Session ends with termination command (exit)   | SNMP response or timeout                       |
| **Security**           | HTTPS (TLS/SSL) for encryption                | DNSSEC, DoH/DoT for encryption and integrity  | FTPS/SFTP for encryption                       | SMTPS (TLS/SSL) for encrypted mail transfer   | SSH (Strong encryption for secure login)       | Telnet has no encryption (plaintext)           | SNMPv3 (Authentication, encryption)             |
| **Encryption**         | HTTPS encrypts all HTTP traffic               | DoH/DoT for encrypted DNS queries             | FTPS/SFTP encrypts both control and data       | SMTPS encrypts email transmission             | SSH encrypts the entire session                | No encryption (plaintext)                      | SNMPv3 offers encryption for sensitive data     |
