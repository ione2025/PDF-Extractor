"""
PDF Tools Module
Comprehensive PDF manipulation functionality
"""
import os
import io
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from PyPDF2.constants import UserAccessPermissions
import fitz  # PyMuPDF
from PIL import Image
import img2pdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.utils import ImageReader
from pdf2image import convert_from_path
from docx import Document
from docx.shared import Inches


class PDFMerger:
    """Merge multiple PDF files into one"""
    
    @staticmethod
    def merge_pdfs(pdf_files, output_path):
        """Merge multiple PDF files"""
        merger = PdfMerger()
        
        for pdf_file in pdf_files:
            merger.append(pdf_file)
        
        merger.write(output_path)
        merger.close()
        
        return output_path


class PDFSplitter:
    """Split PDF into multiple files or extract specific pages"""
    
    @staticmethod
    def split_by_pages(pdf_path, output_dir, pages_per_file=1):
        """Split PDF into separate files"""
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)
        
        output_files = []
        for i in range(0, total_pages, pages_per_file):
            writer = PdfWriter()
            
            for j in range(i, min(i + pages_per_file, total_pages)):
                writer.add_page(reader.pages[j])
            
            output_file = os.path.join(output_dir, f'split_{i//pages_per_file + 1}.pdf')
            with open(output_file, 'wb') as f:
                writer.write(f)
            
            output_files.append(output_file)
        
        return output_files
    
    @staticmethod
    def extract_pages(pdf_path, output_path, page_numbers):
        """Extract specific pages from PDF"""
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        for page_num in page_numbers:
            if 0 <= page_num < len(reader.pages):
                writer.add_page(reader.pages[page_num])
        
        with open(output_path, 'wb') as f:
            writer.write(f)
        
        return output_path


class PDFRotator:
    """Rotate PDF pages"""
    
    @staticmethod
    def rotate_pages(pdf_path, output_path, rotation=90, pages='all'):
        """Rotate pages by specified angle"""
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        total_pages = len(reader.pages)
        
        for i in range(total_pages):
            page = reader.pages[i]
            
            if pages == 'all' or i in pages:
                page.rotate(rotation)
            
            writer.add_page(page)
        
        with open(output_path, 'wb') as f:
            writer.write(f)
        
        return output_path


class PDFCompressor:
    """Compress PDF file size"""
    
    @staticmethod
    def compress_pdf(pdf_path, output_path, quality='medium'):
        """Compress PDF using PyMuPDF"""
        doc = fitz.open(pdf_path)
        
        # Quality settings
        quality_map = {
            'low': (50, 100),
            'medium': (75, 150),
            'high': (90, 200)
        }
        
        image_quality, image_dpi = quality_map.get(quality, quality_map['medium'])
        
        # Compress images in PDF
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # Get images
            image_list = page.get_images()
            
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                
                # Compress image
                image = Image.open(io.BytesIO(image_bytes))
                
                # Resize if too large
                if image.width > image_dpi or image.height > image_dpi:
                    image.thumbnail((image_dpi, image_dpi), Image.Resampling.LANCZOS)
                
                # Compress
                output_buffer = io.BytesIO()
                image.save(output_buffer, format='JPEG', quality=image_quality, optimize=True)
                
                # Replace image in PDF
                # Note: This is a simplified approach
        
        doc.save(output_path, garbage=4, deflate=True, clean=True)
        doc.close()
        
        return output_path


class PDFConverter:
    """Convert PDF to various formats and vice versa"""
    
    @staticmethod
    def pdf_to_images(pdf_path, output_dir, format='PNG', dpi=200):
        """Convert PDF pages to images"""
        images = convert_from_path(pdf_path, dpi=dpi)
        
        output_files = []
        for i, image in enumerate(images):
            output_file = os.path.join(output_dir, f'page_{i+1}.{format.lower()}')
            image.save(output_file, format)
            output_files.append(output_file)
        
        return output_files
    
    @staticmethod
    def images_to_pdf(image_paths, output_path):
        """Convert multiple images to a single PDF"""
        with open(output_path, 'wb') as f:
            f.write(img2pdf.convert(image_paths))
        
        return output_path
    
    @staticmethod
    def pdf_to_text_file(pdf_path, output_path):
        """Convert PDF to plain text file"""
        doc = fitz.open(pdf_path)
        text = ""
        
        for page in doc:
            text += page.get_text()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        doc.close()
        return output_path
    
    @staticmethod
    def pdf_to_word(pdf_path, output_path):
        """Convert PDF to Word document (basic conversion)"""
        doc = fitz.open(pdf_path)
        word_doc = Document()
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            
            # Add text to Word document
            word_doc.add_paragraph(text)
            
            # Add page break except for last page
            if page_num < len(doc) - 1:
                word_doc.add_page_break()
        
        word_doc.save(output_path)
        doc.close()
        
        return output_path


class PDFWatermark:
    """Add watermarks to PDF"""
    
    @staticmethod
    def add_text_watermark(pdf_path, output_path, watermark_text, opacity=0.3):
        """Add text watermark to PDF"""
        doc = fitz.open(pdf_path)
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # Get page dimensions
            rect = page.rect
            
            # Add watermark
            text_length = fitz.get_text_length(watermark_text, fontsize=50)
            x = (rect.width - text_length) / 2
            y = rect.height / 2
            
            page.insert_text(
                (x, y),
                watermark_text,
                fontsize=50,
                color=(0.5, 0.5, 0.5),
                rotate=45,
                opacity=opacity
            )
        
        doc.save(output_path)
        doc.close()
        
        return output_path
    
    @staticmethod
    def add_image_watermark(pdf_path, output_path, watermark_image, opacity=0.3):
        """Add image watermark to PDF"""
        doc = fitz.open(pdf_path)
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            rect = page.rect
            
            # Calculate watermark position (center)
            img = Image.open(watermark_image)
            img_width, img_height = img.size
            
            # Scale image to fit page
            scale = min(rect.width / img_width, rect.height / img_height) * 0.5
            new_width = img_width * scale
            new_height = img_height * scale
            
            x = (rect.width - new_width) / 2
            y = (rect.height - new_height) / 2
            
            # Insert image
            page.insert_image(
                fitz.Rect(x, y, x + new_width, y + new_height),
                filename=watermark_image,
                opacity=opacity
            )
        
        doc.save(output_path)
        doc.close()
        
        return output_path


class PDFSecurity:
    """PDF encryption and password protection"""
    
    @staticmethod
    def encrypt_pdf(pdf_path, output_path, user_password, owner_password=None):
        """Encrypt PDF with password using PyPDF2
        
        Note: Uses 128-bit encryption (RC4). PyPDF2 does not support AES-256 encryption.
        This provides adequate security for most use cases and maintains compatibility.
        """
        if owner_password is None:
            owner_password = user_password
        
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        # Copy all pages
        for page in reader.pages:
            writer.add_page(page)
        
        # Encrypt with 128-bit encryption
        writer.encrypt(user_password=user_password, owner_password=owner_password, use_128bit=True)
        
        with open(output_path, 'wb') as f:
            writer.write(f)
        
        return output_path
    
    @staticmethod
    def decrypt_pdf(pdf_path, output_path, password):
        """Remove password from PDF"""
        reader = PdfReader(pdf_path, password=password)
        writer = PdfWriter()
        
        # Copy all pages (decrypted)
        for page in reader.pages:
            writer.add_page(page)
        
        with open(output_path, 'wb') as f:
            writer.write(f)
        
        return output_path
    
    @staticmethod
    def set_permissions(pdf_path, output_path, password, allow_printing=True, 
                       allow_modification=False, allow_copying=True):
        """Set PDF permissions using PyPDF2"""
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        # Copy all pages
        for page in reader.pages:
            writer.add_page(page)
        
        # Build permissions flag
        permissions = 0
        if allow_printing:
            permissions |= UserAccessPermissions.PRINT
        if allow_modification:
            permissions |= UserAccessPermissions.MODIFY
        if allow_copying:
            permissions |= UserAccessPermissions.EXTRACT
        
        # Encrypt with permissions
        writer.encrypt(
            user_password=password, 
            owner_password=password, 
            use_128bit=True,
            permissions_flag=permissions
        )
        
        with open(output_path, 'wb') as f:
            writer.write(f)
        
        return output_path


class PDFMetadata:
    """Edit PDF metadata"""
    
    @staticmethod
    def edit_metadata(pdf_path, output_path, title=None, author=None, 
                     subject=None, keywords=None):
        """Edit PDF metadata using PyPDF2"""
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        # Copy all pages
        for page in reader.pages:
            writer.add_page(page)
        
        # Build metadata dictionary
        metadata = {}
        if title:
            metadata['/Title'] = title
        if author:
            metadata['/Author'] = author
        if subject:
            metadata['/Subject'] = subject
        if keywords:
            metadata['/Keywords'] = keywords
        
        # Add metadata
        if metadata:
            writer.add_metadata(metadata)
        
        with open(output_path, 'wb') as f:
            writer.write(f)
        
        return output_path
    
    @staticmethod
    def get_metadata(pdf_path):
        """Get PDF metadata"""
        reader = PdfReader(pdf_path)
        metadata = {}
        
        if reader.metadata:
            for key, value in reader.metadata.items():
                metadata[key] = str(value)
        
        return metadata


class PDFPageManager:
    """Manage PDF pages (delete, reorder, etc.)"""
    
    @staticmethod
    def delete_pages(pdf_path, output_path, pages_to_delete):
        """Delete specific pages from PDF"""
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        total_pages = len(reader.pages)
        
        for i in range(total_pages):
            if i not in pages_to_delete:
                writer.add_page(reader.pages[i])
        
        with open(output_path, 'wb') as f:
            writer.write(f)
        
        return output_path
    
    @staticmethod
    def reorder_pages(pdf_path, output_path, new_order):
        """Reorder PDF pages"""
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        for page_num in new_order:
            if 0 <= page_num < len(reader.pages):
                writer.add_page(reader.pages[page_num])
        
        with open(output_path, 'wb') as f:
            writer.write(f)
        
        return output_path
    
    @staticmethod
    def add_blank_pages(pdf_path, output_path, positions, page_size=(612, 792)):
        """Add blank pages at specified positions"""
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        for i in range(len(reader.pages)):
            if i in positions:
                # Add blank page
                blank_page = writer.add_blank_page(width=page_size[0], height=page_size[1])
            
            writer.add_page(reader.pages[i])
        
        with open(output_path, 'wb') as f:
            writer.write(f)
        
        return output_path


class PDFAnnotation:
    """Add annotations, highlights, and comments to PDF"""
    
    @staticmethod
    def add_text_annotation(pdf_path, output_path, page_num, x, y, text, color=(1, 1, 0)):
        """Add text annotation to PDF"""
        doc = fitz.open(pdf_path)
        
        if 0 <= page_num < len(doc):
            page = doc[page_num]
            
            # Add annotation
            annot = page.add_text_annot((x, y), text)
            annot.set_colors({"stroke": color})
            annot.update()
        
        doc.save(output_path)
        doc.close()
        
        return output_path
    
    @staticmethod
    def add_highlight(pdf_path, output_path, page_num, rect, color=(1, 1, 0)):
        """Add highlight to PDF"""
        doc = fitz.open(pdf_path)
        
        if 0 <= page_num < len(doc):
            page = doc[page_num]
            
            # Add highlight
            highlight = page.add_highlight_annot(rect)
            highlight.set_colors({"stroke": color, "fill": color})
            highlight.set_opacity(0.5)
            highlight.update()
        
        doc.save(output_path)
        doc.close()
        
        return output_path


class PDFOptimizer:
    """Optimize PDF for web, print, or size"""
    
    @staticmethod
    def optimize_for_web(pdf_path, output_path):
        """Optimize PDF for web viewing"""
        doc = fitz.open(pdf_path)
        doc.save(
            output_path,
            garbage=4,
            deflate=True,
            clean=True,
            linear=True  # Linearize for fast web viewing
        )
        doc.close()
        
        return output_path
    
    @staticmethod
    def reduce_file_size(pdf_path, output_path):
        """Reduce PDF file size aggressively"""
        doc = fitz.open(pdf_path)
        doc.save(
            output_path,
            garbage=4,
            deflate=True,
            clean=True,
            pretty=False
        )
        doc.close()
        
        return output_path
