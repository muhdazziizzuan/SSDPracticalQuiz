#!/bin/bash

# SonarQube Setup Script
# This script configures SonarQube with custom admin credentials

echo "Waiting for SonarQube to start..."

# Wait for SonarQube to be ready
until curl -s http://localhost:9000/api/system/status | grep -q '"status":"UP"'; do
    echo "SonarQube is not ready yet. Waiting..."
    sleep 10
done

echo "SonarQube is ready. Configuring admin credentials..."

# Change default admin password
# Default credentials are admin/admin
curl -u admin:admin -X POST "http://localhost:9000/api/users/change_password" \
  -d "login=admin" \
  -d "password=2301955@SIT.singaporetech.edu.sg" \
  -d "previousPassword=admin"

if [ $? -eq 0 ]; then
    echo "✅ Admin password successfully changed to: 2301955@SIT.singaporetech.edu.sg"
else
    echo "❌ Failed to change admin password"
fi

echo "SonarQube setup completed!"
echo "Access SonarQube at: http://127.0.0.1:9000/"
echo "Username: admin"
echo "Password: 2301955@SIT.singaporetech.edu.sg"