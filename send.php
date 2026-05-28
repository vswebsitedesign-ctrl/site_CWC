<?php
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    exit('Method not allowed');
}

$to      = 'info@cornwallwasteclearance.co.uk';
$subject = 'New Enquiry — Cornwall Waste Clearance';

$first_name     = htmlspecialchars(trim($_POST['first_name'] ?? $_POST['first-name'] ?? ''));
$surname        = htmlspecialchars(trim($_POST['surname'] ?? ''));
$telephone      = htmlspecialchars(trim($_POST['telephone'] ?? ''));
$postcode       = htmlspecialchars(trim($_POST['postcode'] ?? ''));
$message        = htmlspecialchars(trim($_POST['message'] ?? ''));

$clearance_type = $_POST['clearance_type'] ?? $_POST['clearance-type'] ?? '';
if (is_array($clearance_type)) {
    $clearance_type = implode(', ', array_map('htmlspecialchars', $clearance_type));
} else {
    $clearance_type = htmlspecialchars($clearance_type);
}

$body = "Name: {$first_name} {$surname}\n"
      . "Telephone: {$telephone}\n"
      . "Postcode: {$postcode}\n"
      . "Clearance Type: {$clearance_type}\n"
      . "Message:\n{$message}\n";

$headers = "From: noreply@cornwallwasteclearance.co.uk\r\n"
         . "Reply-To: {$telephone}\r\n"
         . "X-Mailer: PHP/" . phpversion();

if (mail($to, $subject, $body, $headers)) {
    header('Location: /contact-us/?sent=1');
} else {
    header('Location: /contact-us/?error=1');
}
exit;
