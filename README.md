# 🏙️ Smart City AI-Powered Multilingual Complaint CRM
📌 Project Overview

Municipal corporations receive citizen complaints through multiple channels such as helplines, WhatsApp, social media, web portals, and physical offices. These complaints are often submitted in different regional languages, creating communication barriers and inefficiencies in classification, tracking, and resolution.

This project presents a centralized AI-powered Smart City CRM system that automatically detects language, translates complaints, classifies issues, assigns departments, and tracks SLA performance with real-time dashboards.

The system improves transparency, accountability, and data-driven governance.

🚨 Problem Statement

Complaints are misclassified or delayed due to language barriers and fragmented reporting systems.

Lack of centralized tracking results in poor SLA monitoring, low transparency, and limited urban analytics.

✅ Proposed Solution

The system provides a centralized Smart City CRM integrated with AI capabilities to automate complaint management.

1️⃣ Centralized Complaint Collection

Unified platform to collect complaints from:

Flutter Mobile App

Web Portal

WhatsApp Chatbot (API integration)

All complaints stored in a centralized database (Supabase/Firebase).

2️⃣ AI-Based Language Detection & Translation

Automatic language detection for multilingual complaints.

Real-time translation to a primary administrative language (e.g., English).

Ensures consistent processing regardless of input language.

3️⃣ Automated Issue Classification

NLP-based classification into categories:

Water Supply

Roads & Infrastructure

Electricity

Sanitation

Generates confidence score for classification.

Enables accurate department routing.

4️⃣ Smart Department Assignment

Auto-assignment of complaints based on issue category.

Configurable department mapping logic.

Reduces manual workload and delays.

5️⃣ SLA Monitoring & Escalation

Predefined SLA per complaint category.

Real-time status tracking.

Automated alerts if SLA is breached.

Escalation to higher authority when required.

6️⃣ Governance Dashboard & Heatmaps

Admin dashboard (Flutter Web) for:

Live complaint tracking

Department performance monitoring

Resolution rate analytics

Location-based heatmaps for urban planning

Enables data-driven decision making.

🏗️ System Architecture

User (Mobile/Web/WhatsApp)
↓
Flutter Frontend
↓
Backend (Supabase / Firebase)
↓
AI Processing Layer (Language Detection + NLP Classification)
↓
Department Assignment + SLA Engine
↓
Admin Dashboard + Analytics

🛠️ Tech Stack
🎯 Frontend

Flutter

Cross-platform mobile app (Android)

Flutter Web for Admin Dashboard

Google Maps integration for heatmaps

Real-time UI updates

🔥 Backend (Free Options)
Option 1: Supabase (Recommended for SQL-based system)

Supabase (PostgreSQL Database)

Supabase Auth

Supabase Realtime

Edge Functions for AI processing

Row Level Security (RLS) for secure access

Option 2: Firebase (NoSQL Option)

Firebase Firestore

Firebase Authentication

Firebase Cloud Functions

Firebase Hosting (Web dashboard)

Firebase Cloud Messaging (Notifications)

Both options provide free tiers suitable for prototype and academic projects.

🤖 AI & Automation

Language Detection (ML API / Pretrained Model)

Translation API

NLP Text Classification (TF-IDF + ML model / Lightweight Transformer)

Rule-based SLA engine

Sentiment or priority scoring (optional enhancement)

📊 Analytics & Visualization

Google Maps API (Heatmap Layer)

Chart visualization in Flutter

Real-time complaint statistics

Department performance metrics

🌟 Key Features

Multilingual complaint handling

Automatic translation and classification

Centralized tracking system

Smart department assignment

SLA monitoring and auto-escalation

Governance analytics dashboard

Heatmap-based urban insights

Real-time updates

📈 Impact

Faster complaint resolution

Reduced manual errors

Improved transparency

Better governance monitoring

Data-driven urban planning

Enhanced citizen satisfaction

🔮 Future Enhancements

Predictive complaint clustering

Priority detection using sentiment analysis

Integration with IoT sensors (e.g., water leakage detection)

AI chatbot with voice support

Ward-level performance ranking

👨‍💻 Developed By

Shreyash Zalke
Electronics & Telecommunication Engineering
Smart Governance & AI Enthusiast
