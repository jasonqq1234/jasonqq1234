import os
from PIL import Image, ImageDraw, ImageFont

def generate_tickets(qr_folder_path, output_folder, total_tickets):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Read all QR code images
    qr_images = [img for img in os.listdir(qr_folder_path) if img.endswith(('.png', '.jpg', '.jpeg'))]
    
    # Check if there are enough QR code images
    if len(qr_images) < total_tickets:
        print(f"Warning: Only {len(qr_images)} QR codes available, but {total_tickets} tickets requested.")
        total_tickets = len(qr_images)
    
    for i in range(total_tickets):
        # Create ticket, adjust for vertical long strip
        ticket = Image.new('RGB', (300, 600), 'white')
        draw = ImageDraw.Draw(ticket)
        
        # Try to load a font
        try:
            font = ImageFont.truetype("arial.ttf", 20)  # Adjust font size to 20
        except IOError:
            font = ImageFont.load_default()
        
        # Add text
        texts = [
            f"Ticket #{i+1}",
            f"Train No: G{i+100}",
            f"Seat No: {i%100+1}",
            f"Departure Time: 09:{str(i%60).zfill(2)}",
            f"From: Beijing South",
            f"To: Shanghai Hongqiao"
        ]
        y = 20
        for text in texts:
            draw.text((50, y), text, fill="black", font=font)
            y += 40  # Update y coordinate for the next line of text
        
        # Read and embed QR code
        qr_path = os.path.join(qr_folder_path, qr_images[i % len(qr_images)])
        qr_code = Image.open(qr_path)
        qr_code = qr_code.resize((200, 200))  # Adjust QR code size
        ticket.paste(qr_code, (50, y))  # Adjust QR code position to be below the text
        
        # Save ticket
        ticket.save(os.path.join(output_folder, f"ticket_{i+1}.png"))
        
    print(f"Generated {total_tickets} tickets with QR codes.")

# Example usage, saving generated tickets in "qqq" folder
generate_tickets("QRCODE", "qqq", 100)
