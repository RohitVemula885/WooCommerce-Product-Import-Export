# WooCommerce Product Import Export Plugin

A comprehensive WordPress plugin for importing and exporting WooCommerce products with complete meta data support.

## Features

- **Complete Product Export**: Export all WooCommerce product data including meta fields, custom fields, attributes, variations, and more
- **Flexible Import Options**: Import products with options to update existing products, skip images, or preserve IDs
- **JSON Format**: Uses JSON format for easy data manipulation and readability
- **Admin Interface**: User-friendly admin pages for import and export operations
- **Progress Tracking**: Real-time progress bars during import/export operations
- **Error Handling**: Comprehensive error reporting and handling
- **Meta Data Support**: Full support for all product meta data and custom fields
- **Variation Support**: Complete support for variable products and their variations

## Installation

1. Upload the plugin files to the `/wp-content/plugins/woocommerce-product-import-export/` directory
2. Activate the plugin through the 'Plugins' screen in WordPress
3. Use the 'Product I/E' menu item in your WordPress admin to access the plugin

## Requirements

- WordPress 5.0 or higher
- WooCommerce 3.0 or higher
- PHP 7.4 or higher

## Usage

### Exporting Products

1. Navigate to **Product I/E > Export** in your WordPress admin
2. Configure export settings:
   - Select product statuses (Published, Draft, Private, Trash)
   - Choose product types (Simple, Variable, Grouped, External)
   - Set date range (optional)
3. Click "Export Products"
4. Download the generated JSON file

### Importing Products

1. Navigate to **Product I/E > Import** in your WordPress admin
2. Select your JSON export file
3. Configure import options:
   - **Update existing products**: Update products that already exist (matched by SKU)
   - **Skip image import**: Skip importing product images
   - **Preserve product IDs**: Attempt to preserve original product IDs (may cause conflicts)
4. Click "Import Products"

## JSON Structure

The plugin exports products in the following JSON structure:

```json
{
  "version": "1.0.0",
  "export_date": "2024-01-01 12:00:00",
  "site_url": "https://yoursite.com",
  "products": [
    {
      "id": 123,
      "name": "Product Name",
      "slug": "product-name",
      "type": "simple",
      "status": "publish",
      "sku": "PROD-123",
      "price": "29.99",
      "regular_price": "29.99",
      "sale_price": "",
      "description": "Product description",
      "short_description": "Short description",
      "categories": [...],
      "tags": [...],
      "attributes": [...],
      "meta_data": [...],
      "custom_fields": {...},
      "variations": [...]
    }
  ]
}
```

## Exported Data Fields

The plugin exports the following product data:

### Basic Product Information
- ID, Name, Slug, Type, Status
- Description, Short Description
- SKU, Price, Regular Price, Sale Price
- Sale dates, Total Sales

### Inventory & Shipping
- Tax Status, Tax Class
- Stock Management, Stock Quantity, Stock Status
- Backorders, Low Stock Amount
- Weight, Dimensions (Length, Width, Height)

### Product Relationships
- Categories, Tags, Shipping Class
- Upsells, Cross-sells, Parent Product
- Grouped Products, External Product URL

### Advanced Features
- Product Attributes, Default Attributes
- Variable Product Variations
- Downloadable Files, Download Limits
- Product Images, Gallery Images
- Reviews Settings, Purchase Notes

### Meta Data
- All product meta fields
- Custom fields
- Third-party plugin data

## Import Options

### Update Existing Products
When enabled, the plugin will update existing products that match the imported SKU. If disabled, duplicate SKUs will be skipped.

### Skip Image Import
When enabled, product images and gallery images will not be imported. This is useful when images are not available or you want to preserve existing images.

### Preserve Product IDs
When enabled, the plugin will attempt to use the original product IDs from the export. This may cause conflicts if products with those IDs already exist.

## Error Handling

The plugin provides comprehensive error reporting:

- **Import Errors**: Shows which products failed to import and why
- **Validation Errors**: Alerts for invalid file formats or missing required data
- **Permission Errors**: Checks for proper user capabilities
- **File Size Limits**: Validates file size before processing

## Limitations

- Maximum file size: 50MB
- Large imports may take several minutes to complete
- Image imports require the images to be accessible at their original URLs
- Some third-party plugin data may require additional mapping

## Support

For support, feature requests, or bug reports, please contact the plugin developer.

## Changelog

### 1.0.0
- Initial release
- Basic import/export functionality
- Support for all standard WooCommerce product fields
- Variable product support
- Meta data and custom fields support
- Admin interface with progress tracking

## License

This plugin is licensed under the GPL v2 or later.

## Credits

Developed for WooCommerce product management and migration needs.